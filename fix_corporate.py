import os
import re

f = 'corporate.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '60 day guests &middot; up to 34 adults overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement',
    'Up to 60 day guests &middot; up to 34 adults overnight at Orchid Tree'
)

c = c.replace(
    'Up to 60 day guests &middot; up to 34 adults overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement &middot; 45 min from Whitefield',
    'Up to 60 day guests &middot; up to 34 adults overnight at Orchid Tree &middot; 45 min from Whitefield'
)

c = c.replace(
    '''Yes. Orchid Tree accommodates up to 34 adults overnight across its 11 rooms. Additional accommodation can bring the combined Orchid Tree + Viva Farm capacity to approximately 60 guests, by arrangement.''',
    '''Yes. Overnight accommodation at Orchid Tree is available for up to 34 adults.'''
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
