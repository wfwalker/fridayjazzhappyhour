import os
import sys
import json
import argparse
import datetime
import requests

def load_secrets(secrets_path="mailchimp_secrets.json"):
    """Loads the Mailchimp API key from the local secrets JSON file."""
    if not os.path.exists(secrets_path):
        print(f"\nError: Missing secrets file '{secrets_path}'.", file=sys.stderr)
        print("Please create this file in the project root with your Mailchimp API key:", file=sys.stderr)
        print("{\n  \"api_key\": \"YOUR_MAILCHIMP_API_KEY_HERE\"\n}", file=sys.stderr)
        sys.exit(1)
        
    try:
        with open(secrets_path, 'r') as f:
            data = json.load(f)
        api_key = data.get("api_key")
        if not api_key:
            raise ValueError("Key 'api_key' not found in JSON.")
        return api_key
    except Exception as e:
        print(f"Error reading {secrets_path}: {e}", file=sys.stderr)
        sys.exit(1)

def get_mailchimp_session(api_key):
    """Parses the datacenter from the API key and initializes a requests Session."""
    if '-' not in api_key:
        print("Error: Invalid Mailchimp API key format (missing '-' data center suffix).", file=sys.stderr)
        sys.exit(1)
        
    dc = api_key.split('-')[-1]
    base_url = f"https://{dc}.api.mailchimp.com/3.0"
    
    session = requests.Session()
    session.auth = ('username', api_key)
    session.headers.update({"Content-Type": "application/json"})
    
    return session, base_url

def find_last_sent_campaign(session, base_url):
    """Finds the most recently sent campaign to use as a template."""
    print("Fetching last sent campaign details...")
    url = f"{base_url}/campaigns"
    params = {
        "status": "sent",
        "count": 1,
        "sort_field": "send_time",
        "sort_dir": "DESC"
    }
    
    response = session.get(url, params=params)
    if response.status_code != 200:
        print(f"Error fetching campaigns: {response.status_code} - {response.text}", file=sys.stderr)
        sys.exit(1)
        
    items = response.json().get("campaigns", [])
    if not items:
        print("Error: No previously sent campaigns found to replicate.", file=sys.stderr)
        sys.exit(1)
        
    campaign = items[0]
    print(f"Found template campaign: '{campaign['settings']['title']}' (ID: {campaign['id']})")
    return campaign

def format_date_long(date_obj):
    """Formats a date object to 'Month DD, YYYY' (e.g. July 24, 2026)."""
    return date_obj.strftime("%B %d, %Y")

def update_or_create_merge_field(session, base_url, list_id, tag, name, value):
    """Updates the default value of a list merge field, or creates it if it doesn't exist."""
    print(f"Checking merge field tag '{tag}'...")
    url = f"{base_url}/lists/{list_id}/merge-fields"
    
    # 1. Fetch current list merge fields
    response = session.get(url, params={"count": 50})
    if response.status_code != 200:
        print(f"  Error fetching merge fields: {response.status_code} - {response.text}", file=sys.stderr)
        return False
        
    merge_fields = response.json().get("merge_fields", [])
    field_id = None
    for field in merge_fields:
        if field["tag"] == tag:
            field_id = field["merge_id"]
            break
            
    if field_id:
        # 2. Update existing default value
        print(f"  Updating merge field '{tag}' default value to: '{value}'...")
        update_url = f"{url}/{field_id}"
        payload = {"default_value": value}
        patch_resp = session.patch(update_url, json=payload)
        if patch_resp.status_code != 200:
            print(f"  Error updating merge field '{tag}': {patch_resp.status_code} - {patch_resp.text}", file=sys.stderr)
            return False
    else:
        # 3. Create new field with target default value
        print(f"  Merge field '{tag}' not found. Creating new field...")
        payload = {
            "name": name,
            "type": "text",
            "tag": tag,
            "default_value": value
        }
        post_resp = session.post(url, json=payload)
        if post_resp.status_code != 200:
            print(f"  Error creating merge field '{tag}': {post_resp.status_code} - {post_resp.text}", file=sys.stderr)
            return False
            
    return True

def main():
    parser = argparse.ArgumentParser(description="Replicate Mailchimp campaign and update its dynamic merge tags.")
    parser.add_argument("--show", required=True, help="Episode number (e.g. 305).")
    parser.add_argument("--date", required=True, help="Date of the show in YYYY-MM-DD format (e.g. 2026-07-24).")
    parser.add_argument("--yt-url", required=True, help="Watch URL of the scheduled YouTube stream.")
    parser.add_argument("--preview-text", default="", help="Custom preview text for the email.")
    parser.add_argument("--headline", default="", help="Custom headline text for the newsletter.")
    parser.add_argument("--auto-schedule", action="store_true", help="Schedule the campaign immediately (default: leaves as draft).")
    
    args = parser.parse_args()
    
    # 1. Parse dates
    try:
        new_date = datetime.datetime.strptime(args.date, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Date must be in YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)
        
    new_date_long = format_date_long(new_date)
    new_show = args.show
    
    headline_val = args.headline or f"Join us this Friday for Friday Jazz Happy Hour #{new_show}!"
    
    # 2. Auth with Mailchimp
    api_key = load_secrets()
    session, base_url = get_mailchimp_session(api_key)
    
    # 3. Retrieve last sent campaign
    last_campaign = find_last_sent_campaign(session, base_url)
    template_campaign_id = last_campaign["id"]
    list_id = last_campaign["recipients"]["list_id"]
    
    # 4. Update List-Level Merge Tags (Dynamic replacements)
    print("\nUpdating Mailchimp List Merge Tags...")
    
    # Update/Create YT_URL
    if not update_or_create_merge_field(session, base_url, list_id, "YT_URL", "YouTube URL", args.yt_url):
        sys.exit(1)
        
    # Update/Create SHOW_NUM
    if not update_or_create_merge_field(session, base_url, list_id, "SHOW_NUM", "Show Number", new_show):
        sys.exit(1)
        
    # Update/Create SHOW_DATE
    if not update_or_create_merge_field(session, base_url, list_id, "SHOW_DATE", "Show Date", new_date_long):
        sys.exit(1)
        
    # Update/Create HEADLINE
    if not update_or_create_merge_field(session, base_url, list_id, "HEADLINE", "Newsletter Headline", headline_val):
        sys.exit(1)
        
    # 5. Replicate template campaign to create a new draft (Preserves visual blocks!)
    print("\nReplicating template campaign...")
    replicate_url = f"{base_url}/campaigns/{template_campaign_id}/actions/replicate"
    response = session.post(replicate_url)
    if response.status_code != 200:
        print(f"Error replicating campaign: {response.status_code} - {response.text}", file=sys.stderr)
        sys.exit(1)
        
    new_campaign = response.json()
    new_campaign_id = new_campaign["id"]
    print(f"Successfully created draft campaign (ID: {new_campaign_id})")
    
    # 6. Update Campaign Settings (Subject line, internal title, preview text)
    print("Updating campaign settings (Subject, Title, Preview Text)...")
    campaign_update_url = f"{base_url}/campaigns/{new_campaign_id}"
    
    subject_title = f"Friday Jazz Happy Hour #{new_show}"
    preview = args.preview_text or f"Join us live on YouTube this Friday at 5:00 PM Pacific!"
    
    settings_body = {
        "settings": {
            "subject_line": subject_title,
            "preview_text": preview,
            "title": f"FJHH #{new_show} Newsletter" # Internal title
        }
    }
    
    settings_response = session.patch(campaign_update_url, json=settings_body)
    if settings_response.status_code != 200:
        print(f"Error updating campaign settings: {settings_response.status_code} - {settings_response.text}", file=sys.stderr)
        sys.exit(1)
    print("  Campaign settings updated.")
    
    # 7. Calculate upcoming Wednesday 9:00 AM schedule time
    days_to_sub = new_date.weekday() - 2 # 2 represents Wednesday
    if days_to_sub <= 0:
        days_to_sub += 7 # Shift to previous week if show date is Wednesday or earlier
        
    wednesday_date = new_date - datetime.timedelta(days=days_to_sub)
    schedule_time_iso = f"{wednesday_date}T09:00:00-07:00"
    
    # 8. Report & Optional Schedule
    print("\n" + "="*40)
    print(" CAMPAIGN CREATION COMPLETE!")
    print("="*40)
    print(f"Internal Name: FJHH #{new_show} Newsletter")
    print(f"Subject Line:  {subject_title}")
    print(f"Preview Text:  {preview}")
    print(f"YT_URL:        {args.yt_url}")
    print(f"SHOW_NUM:      {new_show}")
    print(f"SHOW_DATE:     {new_date_long}")
    print(f"HEADLINE:      {headline_val}")
    print(f"Edit Draft:    https://admin.mailchimp.com/campaigns/show?id={new_campaign['web_id']}")
    
    if args.auto_schedule:
        print(f"Scheduling campaign for Wednesday morning ({wednesday_date} at 9:00 AM)...")
        schedule_url = f"{base_url}/campaigns/{new_campaign_id}/actions/schedule"
        schedule_body = {
            "schedule_time": schedule_time_iso
        }
        sched_response = session.post(schedule_url, json=schedule_body)
        if sched_response.status_code != 204:
            print(f"Error scheduling campaign: {sched_response.status_code} - {sched_response.text}", file=sys.stderr)
            print("Note: Campaign remains saved as a DRAFT. You can schedule it manually via the Edit link above.")
        else:
            print("  Campaign scheduled successfully!")
    else:
        print("Note: Campaign is saved as a DRAFT. Schedule it in the Mailchimp web UI or run with --auto-schedule.")
    print("="*40)

if __name__ == "__main__":
    main()
