import os
import sys
import re
import xml.etree.ElementTree as ET

# Common Ableton section cues and structural labels to ignore as song starts
CUE_BLACKLIST = {
    "INTRO", "VERSE", "CHORUS", "LAST CHORUS", "HEAD", "LAST HEAD", 
    "BREAK", "PICKUP", "BOMP", "VCV OFF", "MELODICER", "OUTRO", "SOLO"
}

def is_valid_song_name(name):
    """Filters out cued markers, cased numbers, and structural track section labels."""
    name = name.strip()
    
    # 1. Must be in ALL CAPS
    if not name.isupper():
        return False
        
    # 2. Filter out single-word structural cues
    if name in CUE_BLACKLIST:
        return False
        
    # 3. Filter out structural markers like A 1, B 2, C 12 (Letter + space + digit)
    if re.match(r'^[A-Z]\s+\d+$', name):
        return False
        
    # 4. Skip single-character labels
    if len(name) <= 1:
        return False
        
    return True

def clean_tempo(tempo_str):
    """Cleans Ableton internal float values into friendly integers or rounded decimals."""
    if not tempo_str:
        return "-"
    try:
        val = float(tempo_str)
        if val.is_integer():
            return str(int(val))
        return f"{val:.1f}" # Round to 1 decimal place (e.g. 115.5)
    except ValueError:
        return tempo_str

def extract_scenes_to_markdown(xml_path, output_md_path):
    """Parses Ableton Live XML file to extract songs, tempos, and arrangement sections."""
    if not os.path.exists(xml_path):
        print(f"Error: File not found: {xml_path}", file=sys.stderr)
        sys.exit(1)
        
    print(f"Parsing Ableton XML file memory-efficiently: {xml_path}...")
    
    songs_list = []
    current_song = None
    all_scenes_count = 0
    
    # Use iterparse to stream the 277MB XML file without loading it all into RAM
    try:
        context = ET.iterparse(xml_path, events=("end",))
        for event, elem in context:
            if elem.tag == "Scene":
                all_scenes_count += 1
                name_elem = elem.find("Name")
                name_val = name_elem.get("Value") if name_elem is not None else ""
                name_clean = name_val.strip() if name_val else ""
                
                # Check if this scene starts a song
                if name_clean and is_valid_song_name(name_clean):
                    tempo_elem = elem.find("Tempo")
                    tempo_val = ""
                    if tempo_elem is not None:
                        tempo_val = tempo_elem.get("Value", "").strip()
                        
                    current_song = {
                        "name": name_clean,
                        "tempo": clean_tempo(tempo_val),
                        "sections": []
                    }
                    songs_list.append(current_song)
                elif current_song is not None:
                    # A blank name terminates the current song's arrangement collection
                    if not name_clean:
                        current_song = None
                    else:
                        # Otherwise, add to sections
                        current_song["sections"].append(name_clean)
                
                # Free memory associated with parsed node
                elem.clear()
    except Exception as e:
        print(f"Error parsing XML file: {e}", file=sys.stderr)
        sys.exit(1)
        
    print(f"\nSuccessfully parsed {all_scenes_count} total scenes.")
    
    # Deduplicate entries based on name, tempo, and arrangement sections
    unique_songs = []
    seen = set()
    for song in songs_list:
        sections_str = " → ".join(song["sections"])
        key = (song["name"], song["tempo"], sections_str)
        if key not in seen:
            seen.add(key)
            unique_songs.append({
                "name": song["name"],
                "tempo": song["tempo"],
                "arrangement": sections_str
            })
            
    # Sort songs alphabetically by name
    unique_songs.sort(key=lambda x: x["name"])
    
    print(f"Extracted {len(unique_songs)} unique song arrangements.")
    print(f"Writing Markdown table to: {output_md_path}...")
    
    try:
        with open(output_md_path, "w") as f:
            f.write("# Ableton Live Repertoire & Arrangements\n\n")
            f.write(f"Extract compiled from Ableton Live set on {all_scenes_count} scenes.\n\n")
            f.write("| Song Name | Tempo (BPM) | Arrangement Sections |\n")
            f.write("|---|---|---|\n")
            for song in unique_songs:
                arrangement = song["arrangement"] if song["arrangement"] else "-"
                f.write(f"| {song['name']} | {song['tempo']} | {arrangement} |\n")
        print("Done! Markdown file written successfully.")
    except Exception as e:
        print(f"Error writing to output file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file_path = os.path.join(script_dir, "tmp-xml-extract.xml")
    output_file_path = os.path.join(script_dir, "repertoire.md")
    
    extract_scenes_to_markdown(xml_file_path, output_file_path)
