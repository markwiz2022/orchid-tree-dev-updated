import os

files = ['home.html', 'index.html', 'stays.html', 'orchidtree-dynamic-page-wireframe.html', 'orchidtree-home-wireframe.html', 'shared/content.js']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Common strings
    c = c.replace('<span class="sleeps">Sleeps up to 4</span>', '<span class="sleeps">Sleeps up to 4 (any mix of adults & children)</span>')
    c = c.replace('<span class="sleeps">Sleeps up to 6 guests</span>', '<span class="sleeps">Sleeps up to 6 (any mix of adults & children)</span>')
    c = c.replace('<span class="sleeps">Sleeps up to 6</span>', '<span class="sleeps">Sleeps up to 6 (any mix of adults & children)</span>')
    
    c = c.replace('<span class="v">Up to 4</span>', '<span class="v">Up to 4 (any mix of adults & children)</span>')
    c = c.replace('<span class="v">Up to 6</span>', '<span class="v">Up to 6 (any mix of adults & children)</span>')
    
    # In shared/content.js
    c = c.replace('Family Rooms sleep up to 4.', 'Family Rooms sleep up to 4 guests (any mix of adults and children).')
    c = c.replace('Chandana sleeps up to 6.', 'Chandana sleeps up to 6 guests (any mix of adults and children).')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
