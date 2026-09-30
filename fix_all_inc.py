import os
import re

exact_new = '<p>Your room, breakfast, lunch, dinner, high tea, snacks, wellness inclusions and full estate access are included. Alcohol and separately priced optional extras are not included.</p>'

# For home.html and index.html
for f in ['home.html', 'index.html', 'orchidtree-home-wireframe.html']:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    old1 = '<p>Yes. Every stay includes breakfast, lunch and dinner, freshly prepared to your preferences, along with high tea, snacks, wellness and full estate access. Tell us dietary needs before you arrive.</p>'
    c = c.replace(old1, exact_new)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

# For faq.html
f = 'faq.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old2 = '<p>Yes. Breakfast, lunch and dinner are included, cooked fresh to order. Tell us your preferences and dietary needs before arrival so the kitchen can plan every meal around your stay.</p>'
c = c.replace(old2, exact_new)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

