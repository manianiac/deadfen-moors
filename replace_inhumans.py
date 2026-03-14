import os
import re

vault_dir = '/Users/wbarron/Documents/LARPA TTRPG'

replacements = {
    'index.md': [
        (r'\*\*The \[\[God Kings\|God-Kings\]\] \(Inhumans\):\*\*', r'**The [[God Kings|God-Kings]]:**'),
        (r'engineered inhumans', r'superhuman warriors'),
        (r'inhuman blood', r'powerful blood')
    ],
    'The Deadfen Moors/Characters/Dumuzi.md': [
        (r', inhuman\]', ']'),
        (r'Inhuman \[\[God-Kings', r'[[God-Kings')
    ],
    'The Deadfen Moors/Lore/Elves/Elves.md': [
        (r'Inhuman \[\[God-Kings', r'[[God-Kings')
    ],
    'The Deadfen Moors/Hexes/Rock of the Dead Dumuzi.md': [
        (r'or Inhuman', r'or God-Kings')
    ],
    'The Deadfen Moors/Characters/Vortigern.md': [
        (r', inhuman,', ',')
    ],
    'The Deadfen Moors/Characters/Beric.md': [
        (r', inhuman,', ','),
        (r'An Inhuman champion', r'A champion')
    ],
    'The Deadfen Moors/Characters/Caelen.md': [
        (r', inhuman,', ','),
        (r'An Inhuman champion', r'A champion')
    ],
    'The Deadfen Moors/Characters/Drust.md': [
        (r', inhuman,', ','),
        (r'An Inhuman \[\[God', r'A [[God')
    ]
}

for rel_path, reps in replacements.items():
    filepath = os.path.join(vault_dir, rel_path)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        for old, new in reps:
            content = re.sub(old, new, content)
            
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {rel_path}")

