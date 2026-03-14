import os
import re

contents_file = "/Users/wbarron/Documents/LARPA TTRPG/The Deadfen Moors/Hexes/Contents.md"

with open(contents_file, 'r') as f:
    lines = f.readlines()

final_lines = []

for line in lines:
    raw_line = line.strip()
    
    if raw_line.startswith("|") and "Hex Label" not in raw_line and "---" not in raw_line:
        # Extract Hex Label
        match_hex = re.search(r'([A-Z]\.\d+)', raw_line)
        hex_label = match_hex.group(1) if match_hex else ""
        
        # Clean text to split correctly
        cleaned_text = raw_line.replace('**[[', '').replace(']]**', '').replace('[[', '').replace(']]', '').replace('\\', '').strip()
        parts = [p.strip() for p in cleaned_text.split('|') if p.strip()]
        
        # Determine columns
        hex_val = hex_label
        terrain_val = ""
        name_val = ""
        
        terrains = ["Hills", "Mountains", "Volcano", "Plains", "Forest", "Swamp", "Farmland", "River", "Village", "Plains (with scrub)", "Forest (on hills)"]
        
        for p in parts:
            if p in terrains or any(t in p for t in terrains):
                terrain_val = p
                break
                
        possible_names = [p for p in parts if p != hex_val and p != terrain_val]
        if len(possible_names) > 0:
            name_val = possible_names[-1]
            if not name_val:
                name_val = possible_names[0]
                
        if hex_val == "N.10":
            name_val = "Gundinul Tavern"
            terrain_val = "Plains"
            
        new_row = f"| **[[{hex_val}]]** | {terrain_val} | [[{name_val}]] | |"
        final_lines.append(new_row)
    else:
        final_lines.append(raw_line)

# Auto-align the columns
parsed_rows = []
col_widths = []

for line in final_lines:
    if line.strip().startswith("|") and "---" not in line and "Hex Label" not in line:
        parts = [p.strip() for p in line.strip().split("|")[1:-1]]
        parsed_rows.append(parts)
        while len(col_widths) < len(parts):
            col_widths.append(0)
        for i, p in enumerate(parts):
            col_widths[i] = max(col_widths[i], len(p))
            
    elif line.strip().startswith("|") and "Hex Label" in line:
        parts = [p.strip() for p in line.strip().split("|")[1:-1]]
        while len(parts) < 4: parts.append("")
        parts = parts[:4]
        while len(col_widths) < len(parts):
            col_widths.append(0)
        for i, p in enumerate(parts):
             col_widths[i] = max(col_widths[i], len(p))

out_lines = []
row_idx = 0
for line in final_lines:
    if line.strip().startswith("|") and "---" not in line and "Hex Label" not in line:
        parts = parsed_rows[row_idx]
        while len(parts) < 4: parts.append("")
        parts = parts[:4]
        formatted_parts = []
        for i, p in enumerate(parts):
            formatted_parts.append(p.ljust(col_widths[i]))
        final_line = "| " + " | ".join(formatted_parts) + " |\n"
        out_lines.append(final_line)
        row_idx += 1
    elif line.strip().startswith("|") and "Hex Label" in line:
        parts = [p.strip() for p in line.strip().split("|")[1:-1]]
        while len(parts) < 4: parts.append("")
        parts = parts[:4]
        formatted_parts = []
        for i, p in enumerate(parts):
            formatted_parts.append(p.ljust(col_widths[i]))
        final_line = "| " + " | ".join(formatted_parts) + " |\n"
        out_lines.append(final_line)
    elif line.strip().startswith("|") and "---" in line:
        formatted_parts = ["-" * w for w in col_widths]
        final_line = "| " + " | ".join(formatted_parts) + " |\n"
        out_lines.append(final_line)
    else:
        out_lines.append(line + "\n")

with open(contents_file, 'w') as f:
    f.writelines(out_lines)

print("Formatting successful!")
