import os

files = ['home.html', 'index.html', 'stays.html', 'shared/content.js', 'orchidtree-dynamic-page-wireframe.html', 'experiences.html']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Replace (up to 8) -> (age 0-8)
    c = c.replace('(up to 8)', '(age 0&ndash;8)')
    
    # Replace Children aged 0-8 -> Children (age 0-8)
    c = c.replace('Children aged 0-8', 'Children (age 0-8)')
    c = c.replace('Children aged 7-8', 'Children (age 7-8)')
    c = c.replace('under 8', 'age 0&ndash;8')
    c = c.replace('8 and under', 'age 0&ndash;8')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
