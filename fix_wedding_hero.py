import os

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '.hero-inner{position:relative;z-index:2;padding:0 var(--pad) clamp(40px,7vh,80px);width:100%;}',
    '.hero-inner{position:relative;z-index:2;padding:120px var(--pad) clamp(40px,7vh,80px);width:100%;}'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)