import os
import re

base_dir = "/Users/wbarron/Documents/LARPA TTRPG/The Deadfen Moors"

def fix_grammar(text):
    original_text = text
    
    # Fix 'An'/'an' before 'Scourge' and 'Nabu' (with or without brackets)
    text = re.sub(r'\ban \[\[Scourge', 'a [[Scourge', text)
    text = re.sub(r'\bAn \[\[Scourge', 'A [[Scourge', text)
    text = re.sub(r'\ban Scourge\b', 'a Scourge', text)
    text = re.sub(r'\bAn Scourge\b', 'A Scourge', text)
    
    text = re.sub(r'\ban \[\[Nabu', 'a [[Nabu', text)
    text = re.sub(r'\bAn \[\[Nabu', 'A [[Nabu', text)
    text = re.sub(r'\ban Nabu\b', 'a Nabu', text)
    text = re.sub(r'\bAn Nabu\b', 'A Nabu', text)
    
    # Fix possessives (Nabu' -> Nabu's, Scourge' -> Scourge's) if they exist
    # Be careful not to replace if it is already Nabu's
    text = re.sub(r"\bNabu'(?!s)\b", "Nabu's", text)
    text = re.sub(r"\bScourge'(?!s)\b", "Scourge's", text)
    
    return text

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding='utf-8') as f:
                    content = f.read()
                
                new_content = fix_grammar(content)
                
                if new_content != content:
                    with open(file_path, "w", encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed grammar in {file_path}")

process_directory(base_dir)
