import os
import re

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = re.sub(r'<div class="statband reveal">\s*<div class="s"><div class="big" data-count="200">200</div><div class="lbl">maximum celebration guests</div></div>\s*<div class="s"><div class="big" data-count="60">60</div><div class="lbl">maximum resident guests</div></div>\s*<div class="s"><div class="big" data-count="34">34</div><div class="lbl">approx\. stay at Orchid Tree</div></div>\s*<div class="s"><div class="big" data-count="26">26</div><div class="lbl">approx\. stay at Viva Farm</div></div>\s*</div>', 
'''<div class="statband reveal">
          <div class="s"><div class="big" data-count="200">200</div><div class="lbl">maximum celebration guests</div></div>
          <div class="s"><div class="big" data-count="34">34</div><div class="lbl">maximum overnight adults</div></div>
        </div>''', c)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)