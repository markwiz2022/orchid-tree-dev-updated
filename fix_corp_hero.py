import os
import re

filepath = 'corporate.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div class="hero-stats">.*?</div>'
replacement = '<div class="hero-stats" style="color:rgba(255,255,255,0.9); font-size:15px; letter-spacing:0.5px; font-weight:500; text-align:center;">60 day guests &middot; up to 34 overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement</div>'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
