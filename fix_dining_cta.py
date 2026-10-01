import os

files = ['blog-farm-to-table-dining-near-bangalore.html', 'experiences.html']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    c = c.replace('href="#">Read about dining at Orchid Tree</a>', 'href="blog-farm-to-table-dining-near-bangalore.html">Read about dining at Orchid Tree</a>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
