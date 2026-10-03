import os
import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    if '34 adults' in c or '34 overnight adults' in c:
        c = c.replace('34 adults', '34 guests')
        c = c.replace('34 overnight adults', '34 resident guests')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(c)
