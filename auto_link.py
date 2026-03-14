import os
import re

vault_dir = '/Users/wbarron/Documents/LARPA TTRPG'

# 1. Build dictionary of entities
# We will map lowercase text to the canonical link format.
# If text == title, map to [[Title]]
# If text != title, map to [[Title|Text]] (wait, we'll replace dynamically to preserve case)

titles = {}
aliases_dict = {}

for root, dirs, files in os.walk(vault_dir):
    for dir in ['.gemini', '.git', 'node_modules']:
        if dir in dirs:
            dirs.remove(dir)
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            title = file[:-3]
            titles[title.lower()] = title
            
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                
                match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                if match:
                    fm_text = match.group(1)
                    # simple regex for aliases
                    aliases_match = re.search(r'^aliases:\s*\[(.*?)\]', fm_text, re.MULTILINE)
                    if aliases_match:
                        for a in aliases_match.group(1).split(','):
                            a = a.strip().strip('"\'')
                            if a:
                                aliases_dict[a.lower()] = title
                    else:
                        aliases_match2 = re.search(r'^aliases:\s*(.+)$', fm_text, re.MULTILINE)
                        if aliases_match2:
                            a = aliases_match2.group(1).strip().strip('"\'')
                            if a and not a.startswith('['):
                                aliases_dict[a.lower()] = title
            except:
                pass

# Sort terms by length descending, so we match "God Kings" before "God"
all_terms = list(titles.keys()) + list(aliases_dict.keys())
# Remove short words that might over-match
all_terms = [t for t in all_terms if len(t) > 3 or t == 'Nabu']
# Unique
all_terms = list(set(all_terms))
all_terms.sort(key=len, reverse=True)

# Function to get canonical link
def get_canonical_link(match):
    text = match.group(0)
    lower_text = text.lower()
    
    if lower_text in titles:
        title = titles[lower_text]
        if text == title:
            return f"[[{title}]]"
        return f"[[{title}|{text}]]"
    elif lower_text in aliases_dict:
        title = aliases_dict[lower_text]
        return f"[[{title}|{text}]]"
    return text

# Escape terms for regex
escaped_terms = [re.escape(t) for t in all_terms]
pattern_str = r'\b(' + '|'.join(escaped_terms) + r')\b'
# Case insensitive match
pattern = re.compile(pattern_str, re.IGNORECASE)

def process_text(text):
    # We want to AVOID replacing inside:
    # 1. [[...]]
    # 2. Frontmatter ^---\n...\n--- (already handled if we process text chunks)
    # 3. Headers ^# ...
    # 4. URLs (http...)
    
    # Simple state machine to split text into "safe to replace" and "do not replace" chunks
    # We will use regex to find all protected blocks, and split the string
    
    protected_pattern = re.compile(r'(\[\[.*?\]\]|---\n[\s\S]*?\n---|^\#.*$|https?://[^\s]+)', re.MULTILINE)
    
    chunks = []
    last_end = 0
    for match in protected_pattern.finditer(text):
        start, end = match.span()
        # safe chunk
        if start > last_end:
            chunks.append(("SAFE", text[last_end:start]))
        # protected chunk
        chunks.append(("PROTECTED", text[start:end]))
        last_end = end
        
    if last_end < len(text):
        chunks.append(("SAFE", text[last_end:]))
        
    new_text = ""
    for chunk_type, chunk_text in chunks:
        if chunk_type == "SAFE":
            new_text += pattern.sub(get_canonical_link, chunk_text)
        else:
            new_text += chunk_text
            
    return new_text

updated_count = 0
for root, dirs, files in os.walk(vault_dir):
    for dir in ['.gemini', '.git', 'node_modules']:
        if dir in dirs:
            dirs.remove(dir)
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            new_content = process_text(content)
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                updated_count += 1

print(f"Updated {updated_count} files with new links.")
