import os
import sys
import json
import argparse
import datetime
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

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

def get_mailchimp_client(api_key):
    """Initializes the Mailchimp Marketing Client."""
    if '-' not in api_key:
        print("Error: Invalid Mailchimp API key format (missing '-' data center suffix).", file=sys.stderr)
        sys.exit(1)
        
    dc = api_key.split('-')[-1]
    
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": api_key,
        "server": dc
    })
    return client

def get_default_list_details(client):
    """Fetches the default audience list and extracts list_id and sender details from defaults."""
    print("Fetching audience list details...")
    try:
        response = client.lists.get_all_lists()
        lists = response.get("lists", [])
        if not lists:
            print("Error: No audience lists found in your Mailchimp account.", file=sys.stderr)
            sys.exit(1)
            
        # Prefer "Friday Jazz Happy Hour" list if it exists, otherwise use the first list
        target_list = None
        for l in lists:
            if l["name"].strip().lower() == "friday jazz happy hour":
                target_list = l
                break
        if not target_list:
            target_list = lists[0]
            
        list_id = target_list["id"]
        defaults = target_list.get("campaign_defaults", {})
        from_name = defaults.get("from_name", "Friday Jazz Happy Hour")
        reply_to = defaults.get("from_email", "")
        
        print(f"Using list: '{target_list['name']}' (ID: {list_id})")
        print(f"Default sender: '{from_name}' <{reply_to}>")
        return list_id, from_name, reply_to
    except ApiClientError as error:
        print(f"Error fetching lists: {error.text}", file=sys.stderr)
        sys.exit(1)

def find_campaign_by_title(client, title):
    """Finds a draft campaign ID by its title/name."""
    print(f"Searching for draft campaign named '{title}'...")
    try:
        response = client.campaigns.list(
            status="save",
            count=100,
            fields=["campaigns.id", "campaigns.settings.title"]
        )
        campaigns = response.get("campaigns", [])
        for c in campaigns:
            if c["settings"]["title"].strip().lower() == title.strip().lower():
                print(f"Found draft campaign: '{c['settings']['title']}' (ID: {c['id']})")
                return c["id"]
        return None
    except ApiClientError as error:
        print(f"Error fetching draft campaigns: {error.text}", file=sys.stderr)
        sys.exit(1)

def find_template_by_name(client, template_name):
    """Finds a Mailchimp template ID by its name."""
    print(f"Searching for template: '{template_name}'...")
    try:
        response = client.templates.list(
            count=100,
            fields=["templates.id", "templates.name"]
        )
        templates = response.get("templates", [])
        for t in templates:
            if t["name"].strip().lower() == template_name.strip().lower():
                print(f"Found template: '{t['name']}' (ID: {t['id']})")
                return t["id"]
                
        print(f"Error: Template '{template_name}' not found in Mailchimp account.", file=sys.stderr)
        print("Available templates:", file=sys.stderr)
        for t in templates:
            print(f" - {t['name']} (ID: {t['id']})", file=sys.stderr)
        sys.exit(1)
    except ApiClientError as error:
        print(f"Error fetching templates: {error.text}", file=sys.stderr)
        sys.exit(1)

def format_date_long(date_obj):
    """Formats a date object to 'Month DD, YYYY' (e.g. July 24, 2026)."""
    return date_obj.strftime("%B %d, %Y")

def update_or_create_merge_field(client, list_id, tag, name, value):
    """Updates the default value of a list merge field, or creates it if it doesn't exist."""
    print(f"Checking merge field tag '{tag}'...")
    try:
        response = client.lists.get_list_merge_fields(list_id, count=50)
        merge_fields = response.get("merge_fields", [])
        field_id = None
        for field in merge_fields:
            if field["tag"] == tag:
                field_id = field["merge_id"]
                break
                
        if field_id:
            print(f"  Updating merge field '{tag}' default value to: '{value}'...")
            payload = {"default_value": value}
            client.lists.update_list_merge_field(list_id, field_id, payload)
        else:
            print(f"  Merge field '{tag}' not found. Creating new field...")
            payload = {
                "name": name,
                "type": "text",
                "tag": tag,
                "default_value": value
            }
            client.lists.add_list_merge_field(list_id, payload)
        return True
    except ApiClientError as error:
        print(f"  Error managing merge field '{tag}': {error.text}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Create Mailchimp campaign from a template and update dynamic merge tags.")
    parser.add_argument("--show", required=True, help="Episode number (e.g. 305).")
    parser.add_argument("--date", required=True, help="Date of the show in YYYY-MM-DD format (e.g. 2026-07-24).")
    parser.add_argument("--yt-url", required=True, help="Watch URL of the scheduled YouTube stream.")
    parser.add_argument("--preview-text", default="", help="Custom preview text for the email.")
    parser.add_argument("--headline", default="", help="Custom headline text for the newsletter.")
    parser.add_argument("--template-name", default="FJHH Template v1", help="Name of the Mailchimp template to use (default: 'FJHH Template v1').")
    parser.add_argument("--template-campaign", default="FJHH Template Campaign", help="Name of the master draft campaign to replicate (default: 'FJHH Template Campaign').")
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
    client = get_mailchimp_client(api_key)
    
    # 3. Retrieve list and sender details
    list_id, from_name, reply_to = get_default_list_details(client)
        
    # 4. Update List-Level Merge Tags (Dynamic replacements)
    print("\nUpdating Mailchimp List Merge Tags...")
    
    # Update/Create YT_URL
    if not update_or_create_merge_field(client, list_id, "YT_URL", "YouTube URL", args.yt_url):
        sys.exit(1)
        
    # Update/Create EP_NUM
    if not update_or_create_merge_field(client, list_id, "EP_NUM", "Episode Number", new_show):
        sys.exit(1)
        
    # Update/Create EP_DATE
    if not update_or_create_merge_field(client, list_id, "EP_DATE", "Episode Date", new_date_long):
        sys.exit(1)
        
    # Update/Create HEADLINE
    if not update_or_create_merge_field(client, list_id, "HEADLINE", "Newsletter Headline", headline_val):
        sys.exit(1)
        
    subject_title = f"Friday Jazz Happy Hour #{new_show} for {new_date_long}"
    preview = args.preview_text or f"Join us live on YouTube this Friday at 5:00 PM Pacific!"
    campaign_title = f"Friday Jazz Happy Hour # {new_show} for {new_date_long}"
    
    # Try to find a master draft campaign first (to support New Email Builder templates)
    template_campaign_id = find_campaign_by_title(client, args.template_campaign)
    
    if template_campaign_id:
        print(f"\nReplicating master draft campaign '{args.template_campaign}'...")
        try:
            new_campaign = client.campaigns.replicate(template_campaign_id)
            new_campaign_id = new_campaign["id"]
            print(f"Successfully created draft campaign (ID: {new_campaign_id})")
        except ApiClientError as error:
            print(f"Error replicating campaign: {error.text}", file=sys.stderr)
            sys.exit(1)
            
        print("Updating campaign settings (Subject, Title, Preview Text)...")
        settings_body = {
            "settings": {
                "subject_line": subject_title,
                "preview_text": preview,
                "title": campaign_title
            }
        }
        try:
            client.campaigns.update(new_campaign_id, settings_body)
            print("  Campaign settings updated.")
        except ApiClientError as error:
            print(f"Error updating campaign settings: {error.text}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"\nNo draft campaign named '{args.template_campaign}' found.")
        print(f"Falling back to template-based campaign creation using template '{args.template_name}'...")
        
        # Find template ID by name
        template_id = find_template_by_name(client, args.template_name)
        
        # Create campaign using template
        print(f"Creating new campaign from template '{args.template_name}'...")
        campaign_payload = {
            "type": "regular",
            "recipients": {
                "list_id": list_id
            },
            "settings": {
                "subject_line": subject_title,
                "preview_text": preview,
                "title": campaign_title,
                "from_name": from_name,
                "reply_to": reply_to,
                "template_id": template_id
            }
        }
        
        try:
            new_campaign = client.campaigns.create(campaign_payload)
            new_campaign_id = new_campaign["id"]
            print(f"Successfully created campaign shell (ID: {new_campaign_id})")
        except ApiClientError as error:
            print(f"Error creating campaign: {error.text}", file=sys.stderr)
            sys.exit(1)
        
        # Apply template to campaign content
        print(f"Applying template ID {template_id} to campaign content...")
        content_payload = {
            "template": {
                "id": template_id
            }
        }
        
        try:
            client.campaigns.set_content(new_campaign_id, content_payload)
            print("  Template content applied successfully.")
        except ApiClientError as error:
            print(f"Error applying template content: {error.text}", file=sys.stderr)
            sys.exit(1)
    
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
    print(f"Internal Name: {campaign_title}")
    print(f"Subject Line:  {subject_title}")
    print(f"Preview Text:  {preview}")
    print(f"YT_URL:        {args.yt_url}")
    print(f"EP_NUM:        {new_show}")
    print(f"EP_DATE:       {new_date_long}")
    print(f"HEADLINE:      {headline_val}")
    print(f"Edit Draft:    https://admin.mailchimp.com/campaigns/show?id={new_campaign['web_id']}")
    
    if args.auto_schedule:
        print(f"Scheduling campaign for Wednesday morning ({wednesday_date} at 9:00 AM)...")
        schedule_body = {
            "schedule_time": schedule_time_iso
        }
        try:
            client.campaigns.schedule(new_campaign_id, schedule_body)
            print("  Campaign scheduled successfully!")
        except ApiClientError as error:
            print(f"Error scheduling campaign: {error.text}", file=sys.stderr)
            print("Note: Campaign remains saved as a DRAFT. You can schedule it manually via the Edit link above.")
    else:
        print("Note: Campaign is saved as a DRAFT. Schedule it in the Mailchimp web UI or run with --auto-schedule.")
    print("="*40)

if __name__ == "__main__":
    main()
