import re
import os

titles = {'scourge': 'Scourge'}
aliases_dict = {}

def get_canonical_link(match):
    text = match.group(0)
    lower_text = text.lower()
    
    if lower_text in titles:
        title = titles[lower_text]
        if text == title:
            return f"[[{title}]]"
        return f"[[{title}|{text}]]"
    return text

text = "*(They are mutated by the ancient necrotic ash of the Scourge wars).*"
pattern = re.compile(r'\b(scourge)\b', re.IGNORECASE)

print("Original:", text)
print("Replaced:", pattern.sub(get_canonical_link, text))
