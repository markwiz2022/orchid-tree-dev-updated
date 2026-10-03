import os

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '''<div class="num">~60</div>\n          <div class="lbl">Overnight across Orchid Tree + Viva Farm by arrangement</div>''',
    '''<div class="num">34</div>\n          <div class="lbl">Overnight accommodation for adults</div>'''
)

c = c.replace(
    '''Accommodation for up to approximately 60 resident guests can be arranged across Orchid Tree and associated Viva Farm accommodation, subject to rooming and availability.''',
    '''Orchid Tree can accommodate up to 34 adults overnight.'''
)

c = c.replace(
    '''For overnight stays, up to 34 adults can stay at Orchid Tree across its 11 rooms. Additional accommodation can bring the combined Orchid Tree + Viva Farm capacity to approximately 60 guests, by arrangement and subject to rooming and availability.''',
    '''Orchid Tree can accommodate up to 34 adults overnight.'''
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
