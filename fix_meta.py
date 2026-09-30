import os
import glob

# Fix Meta Descriptions
html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "breakfast included and the run of the estate" in content:
        content = content.replace("breakfast included and the run of the estate", "all three meals, wellness and the run of the estate")
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed meta description in {f}")
