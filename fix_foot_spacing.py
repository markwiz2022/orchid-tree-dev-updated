import os

for f in ['home.html', 'index.html', 'orchidtree-home-wireframe.html']:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Let's just add a bullet between the spans
    c = c.replace('</span><span class="pet no">', '</span> &nbsp;&middot;&nbsp; <span class="pet no">')
    c = c.replace('</span><span class="pet yes">', '</span> &nbsp;&middot;&nbsp; <span class="pet yes">')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

