import os

f = 'experiences.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('the on-site restaurant at Orchid Tree', 'Orchid Tree kitchen')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
