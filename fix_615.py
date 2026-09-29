import os
import glob

# Replace "615" with "670" in JSON-LD structured data and stays.html visible text
html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if '"reviewCount": "615"' in content:
        content = content.replace('"reviewCount": "615"', '"reviewCount": "670"')
        modified = True
        
    if '4.4 from 615 guests, and counting' in content:
        content = content.replace('4.4 from 615 guests, and counting', '4.4 from 670+ Google reviews')
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
