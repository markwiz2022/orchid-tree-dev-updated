import os

f = 'blog-intimate-wedding-venues-near-bangalore.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '''<p>Orchid Tree has 11 onsite rooms accommodating up to 34 adults overnight. Additional accommodation for up to approximately 60 resident guests in total can be arranged through associated Viva Farm accommodation, subject to rooming and availability.</p>''',
    '''<p>Orchid Tree accommodates up to 34 adults overnight.</p>'''
)

c = c.replace(
    '''<p>Up to 34 adults can stay overnight at Orchid Tree's 11 rooms. Additional accommodation for up to approximately 60 resident guests in total can be arranged through associated Viva Farm accommodation, subject to rooming and availability. For the ceremony and celebration itself, the estate can welcome up to two hundred guests across the day. The full-estate buyout means no other visitors are on the property during your celebration.</p>''',
    '''<p>Celebrations can accommodate up to 200 guests, with overnight accommodation for up to 34 adults at Orchid Tree. The full-estate buyout means no other visitors are on the property during your celebration.</p>'''
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
