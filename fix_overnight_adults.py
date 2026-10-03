import os
import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    if 'overnight adults' in c:
        c = c.replace('overnight adults', 'overnight guests')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(c)
