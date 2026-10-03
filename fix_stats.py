import os
import re

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = re.sub(r'<div class="num">~60</div>\s*<div class="lbl">Overnight across Orchid Tree \+ Viva Farm by arrangement</div>', r'<div class="num">34</div>\n          <div class="lbl">Overnight accommodation for adults</div>', c)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

f2 = 'weddings.html'
with open(f2, 'r', encoding='utf-8') as file:
    c2 = file.read()

c2 = re.sub(r'<div class="stats reveal" id="wStats">.*?</div>\s*</div>\s*</div>\s*</div>', r'<div class="stats reveal" id="wStats">\n          <div class="s"><div class="big" data-count="200">200</div><div class="lbl">maximum celebration guests</div></div>\n          <div class="s"><div class="big" data-count="34">34</div><div class="lbl">maximum overnight adults</div></div>\n        </div>', c2, flags=re.DOTALL)

with open(f2, 'w', encoding='utf-8') as file:
    file.write(c2)