import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("up to 6", "up to 8")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

file_path2 = 'home.html'
with open(file_path2, 'w', encoding='utf-8') as f:
    f.write(content)
