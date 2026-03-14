import os
import re

vault_dir = '/Users/wbarron/Documents/LARPA TTRPG'

renames = [
    ("The Deadfen Moors/Lore/Abominations.md", "The Deadfen Moors/Lore/Scourge.md"),
    ("The Deadfen Moors/Lore/Precursors.md", "The Deadfen Moors/Lore/Nabu.md")
]

link_replacements = [
    (r'\[\[Abominations\]\]', r'[[Scourge]]'),
    (r'\[\[Abominations\|([^\]]+)\]\]', r'[[Scourge|\1]]'),
    (r'\[\[Precursors\]\]', r'[[Nabu]]'),
    (r'\[\[Precursors\|([^\]]+)\]\]', r'[[Nabu|\1]]'),
    # for God Kings, we might have God Kings|God-Kings so let's simplify them
    (r'\[\[God Kings\|God-Kings\]\]', r'[[God Kings]]')
]

for old_path, new_path in renames:
    full_old = os.path.join(vault_dir, old_path)
    full_new = os.path.join(vault_dir, new_path)
    if os.path.exists(full_old):
        os.rename(full_old, full_new)
        print(f"Renamed {old_path} -> {new_path}")

for root, dirs, files in os.walk(vault_dir):
    for dir in ['.gemini', '.git', 'node_modules']:
        if dir in dirs:
            dirs.remove(dir)
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            orig_content = content
            for old_pat, new_pat in link_replacements:
                content = re.sub(old_pat, new_pat, content)
            
            if content != orig_content:
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"Updated links in {os.path.relpath(filepath, vault_dir)}")
