import os

files = ['home.html', 'index.html', 'orchidtree-home-wireframe.html', 'orchidtree-dynamic-page-wireframe.html', 'stays.html']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()

    # Sticky bar widget
    c = c.replace('<span class="bb-pop-sub">9+</span>', '<span class="bb-pop-sub">(age 9+)</span>')
    c = c.replace('<span class="bb-pop-sub">0-8 years</span>', '<span class="bb-pop-sub">(age 0&ndash;8)</span>')
    
    # Right column widget
    c = c.replace('<span class="rc-sub">9+</span>', '<span class="rc-sub">(age 9+)</span>')
    c = c.replace('<span class="rc-sub">0-8 years</span>', '<span class="rc-sub">(age 0&ndash;8)</span>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

