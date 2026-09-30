import os

filepath = 'experiences.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Read more about the table on the <a href="#" \nstyle="color:var(--gold);padding:0;text-transform:none;letter-spacing:0;font-weight:700;">restaurant</a> page, or \nabout the place itself on <a href="about.html" \nstyle="color:var(--gold);padding:0;text-transform:none;letter-spacing:0;font-weight:700;">about</a>.', 'Read more about the place itself on <a href="about.html" style="color:var(--gold);padding:0;text-transform:none;letter-spacing:0;font-weight:700;">about</a>.')

# If the multi-line replace doesn't work, just regex it.
import re
text = re.sub(r'Read more about the table on the <a href="[^"]*".*?>restaurant</a> page, or \nabout the place itself on <a href="about.html".*?>about</a>\.', 'Read more about the place itself on <a href="about.html" style="color:var(--gold);padding:0;text-transform:none;letter-spacing:0;font-weight:700;">about</a>.', text)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

