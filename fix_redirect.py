import os

files = ['home.html', 'orchidtree-home-wireframe.html']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # insert redirect right after <head>
    for i, line in enumerate(lines):
        if '<head>' in line:
            lines.insert(i+1, '  <script>window.location.replace("/");</script>\n  <meta http-equiv="refresh" content="0; url=/" />\n')
            break
            
    with open(f, 'w', encoding='utf-8') as file:
        file.writelines(lines)

