import os
import re

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '''<div class="sub">Private, nature-led and eco-conscious. Curated end to end for intimate celebrations of up to 200 guests, with accommodation for up to 60 across Orchid Tree and associated Viva Farm accommodation.</div>''',
    '''<div class="sub">Private, nature-led and eco-conscious. Curated end to end for intimate celebrations of up to 200 guests, with overnight accommodation for up to 34 adults at Orchid Tree.</div>'''
)

c = c.replace(
    '''<p class="muted" style="margin-top:16px;max-width:720px;">Up to 200 celebration guests, with accommodation for approximately 60 resident guests across Orchid Tree and associated Viva Farm accommodation.</p>''',
    '''<p class="muted" style="margin-top:16px;max-width:720px;">Up to 200 celebration guests, with overnight accommodation for up to 34 adults at Orchid Tree.</p>'''
)

old_stats = '''        <div class="stats reveal" id="wStats">
          <div class="s"><div class="big" data-count="200">200</div><div class="lbl">maximum celebration guests</div></div>
          <div class="s"><div class="big" data-count="60">60</div><div class="lbl">maximum resident guests</div></div>
          <div class="s"><div class="big" data-count="34">34</div><div class="lbl">approx. stay at Orchid Tree</div></div>
          <div class="s"><div class="big" data-count="26">26</div><div class="lbl">approx. stay at Viva Farm</div></div>
        </div>'''

new_stats = '''        <div class="stats reveal" id="wStats">
          <div class="s"><div class="big" data-count="200">200</div><div class="lbl">maximum celebration guests</div></div>
          <div class="s"><div class="big" data-count="34">34</div><div class="lbl">maximum overnight adults</div></div>
        </div>'''

c = c.replace(old_stats, new_stats)

c = c.replace(
    '''<div class="eyebrow hair" style="color:var(--gold); margin-bottom:8px;">Overnight accommodation</div><p>Up to 34 adults can stay across Orchid Tree's 11 rooms. Children may be accommodated within the room-specific child limits, subject to rooming and availability. Additional accommodation for up to approximately 60 resident guests can be arranged through associated Viva Farm accommodation, subject to rooming and availability.</p>''',
    '''<div class="eyebrow hair" style="color:var(--gold); margin-bottom:8px;">Overnight accommodation</div><p>Up to 34 adults can stay across Orchid Tree's 11 rooms. Children may be accommodated within the room-specific child limits, subject to rooming and availability.</p>'''
)

c = c.replace(
    '''<div class="faq-item"><button class="faq-q">How many people can stay overnight?<span class="plus">+</span></button><div class="faq-a"><p>Up to 34 adults can stay at Orchid Tree itself, with additional accommodation at Viva Farm bringing the combined resident capacity to approximately 60 guests, subject to rooming and availability. Additional hotel rooms nearby can be coordinated separately.</p></div></div>''',
    '''<div class="faq-item"><button class="faq-q">How many people can stay overnight?<span class="plus">+</span></button><div class="faq-a"><p>Overnight accommodation is available for up to 34 adults at Orchid Tree. Additional hotel rooms nearby can be coordinated separately.</p></div></div>'''
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)