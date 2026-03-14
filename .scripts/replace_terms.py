import os
import re

base_dir = "/Users/wbarron/Documents/LARPA TTRPG/The Deadfen Moors"

def replace_terms(text):
    # We want to replace plural and singular
    # For Abomination:
    text = re.sub(r'\bAbominations\b', 'Scourge', text)
    text = re.sub(r'\bAbomination\b', 'Scourge', text)
    # For Precursors:
    text = re.sub(r'\bPrecursors\b', 'Nabu', text)
    text = re.sub(r'\bPrecursor\b', 'Nabu', text)
    return text

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding='utf-8') as f:
                    content = f.read()
                
                new_content = replace_terms(content)
                
                if new_content != content:
                    with open(file_path, "w", encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")

process_directory(base_dir)
