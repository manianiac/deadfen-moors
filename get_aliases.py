import os
import re
import json

vault_dir = '/Users/wbarron/Documents/LARPA TTRPG'
aliases = {}
titles = {}
file_to_h1 = {}

for root, dirs, files in os.walk(vault_dir):
    for dir in ['.gemini', '.git', 'node_modules']:
        if dir in dirs:
            dirs.remove(dir)
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    
                    title = file[:-3]
                    rel_path = os.path.relpath(filepath, vault_dir)
                    titles[title] = rel_path
                    
                    # Match frontmatter
                    rest = content
                    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
                    if match:
                        fm_text = match.group(1)
                        rest = match.group(2)
                        
                        # simple regex for aliases: [a, b] or aliases: a
                        aliases_match = re.search(r'^aliases:\s*\[(.*?)\]', fm_text, re.MULTILINE)
                        if aliases_match:
                            for a in aliases_match.group(1).split(','):
                                a = a.strip().strip('"\'')
                                if a:
                                    aliases[a] = title
                        else:
                            aliases_match2 = re.search(r'^aliases:\s*(.+)$', fm_text, re.MULTILINE)
                            if aliases_match2:
                                a = aliases_match2.group(1).strip().strip('"\'')
                                if a and not a.startswith('['):
                                    aliases[a] = title
                    
                    # Find first H1
                    h1_match = re.search(r'^#\s+(.+)$', rest, re.MULTILINE)
                    if h1_match:
                        h1 = h1_match.group(1).strip()
                        file_to_h1[rel_path] = h1
                        
            except Exception as e:
                print(f"Error reading {filepath}: {e}")

with open('/tmp/vault_data.json', 'w') as f:
    json.dump({
        "aliases": aliases,
        "titles": titles,
        "file_to_h1": file_to_h1
    }, f, indent=2)

print(f"Processed {len(titles)} files.")
print(f"Found {len(file_to_h1)} H1 headings.")
print("Files with differing H1s:")
diff_count = 0
for rel_path, h1 in list(file_to_h1.items()):
    filename = os.path.basename(rel_path)[:-3]
    if h1 != filename:
        if diff_count < 20:
            print(f"  {rel_path}: '{filename}' -> '{h1}'")
        diff_count += 1
print(f"Total files needing rename: {diff_count}")
