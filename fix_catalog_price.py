import os

file_path = 'shared/catalog.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("priceFrom: 13000", "priceFrom: null")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
