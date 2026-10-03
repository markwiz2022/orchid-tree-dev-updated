import os

f = 'blog-farm-to-table-dining-near-bangalore.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    'That is close enough for a day visit, but the dining model is designed around a stay.',
    'That is close enough for a quick drive from the city, but our dining experience is designed around an overnight stay.'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
