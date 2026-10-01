import os

f = 'book-packages.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('<span class="bke-ss">9+</span>', '<span class="bke-ss">(age 9+)</span>')
c = c.replace('<span class="bke-ss">0-8 years</span>', '<span class="bke-ss">(age 0&ndash;8)</span>')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

