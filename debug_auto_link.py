import re
import os

vault_dir = '/Users/wbarron/Documents/LARPA TTRPG'
titles = {}
aliases_dict = {}
for root, dirs, files in os.walk(vault_dir):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            title = file[:-3]
            titles[title.lower()] = title

print("Scourge in titles?", 'scourge' in titles)
