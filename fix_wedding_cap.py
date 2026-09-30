import os
import re

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('<div class="big" data-count="45">45</div><div class="lbl">approx. stay at Orchid Tree</div>', '<div class="big" data-count="34">34</div><div class="lbl">approx. stay at Orchid Tree</div>')
c = c.replace('<div class="big" data-count="15">15</div><div class="lbl">approx. stay at Viva Farm</div>', '<div class="big" data-count="26">26</div><div class="lbl">approx. stay at Viva Farm</div>')

old_darkband = '<p>The wedding can host up to 200 people, but the property is not a 200-room destination resort. Accommodation is intentionally kept to around 60, so the estate stays intimate. Additional hotel rooms nearby can be coordinated separately when needed.</p>'
new_darkband = '<div class="eyebrow hair" style="color:var(--gold); margin-bottom:8px;">Overnight accommodation</div><p>Up to 34 guests can stay across Orchid Tree\'s 11 rooms. Additional accommodation for up to approximately 60 resident guests can be arranged through associated Viva Farm accommodation, subject to rooming and availability.</p>'

c = c.replace(old_darkband, new_darkband)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

