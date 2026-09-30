import os
import re

filepath = 'experiences.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Just remove the specific link tag and the words around it
text = re.sub(r'Read more about the table on the <a href="[^"]*"(.*?)>restaurant</a> page, or (.*?)about the place itself on <a href="about.html"(.*?)>about</a>', r'Read more about the place itself on <a href="about.html"\3>about</a>', text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

