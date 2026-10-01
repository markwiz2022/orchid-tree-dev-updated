import os

f = 'about.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_1 = 'When you are here, the estate belongs to you.'
new_1 = 'When you are here, the estate feels like yours.'
c = c.replace(old_1, new_1)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
