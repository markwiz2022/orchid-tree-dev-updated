import os

f = 'corporate.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('Up to Up to 60 day guests', 'Up to 60 day guests')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)