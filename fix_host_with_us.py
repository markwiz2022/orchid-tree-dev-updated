import os
import re

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Fix stat block
c = c.replace('<div class="lbl">Overnight at Orchid Tree, up to</div>', '<div class="lbl">Adults overnight at Orchid Tree, up to</div>')

# Fix FAQ
old_faq = '<p>Up to sixty for a daytime gathering and up to thirty-four staying overnight across the eleven rooms. We keep it intimate by design.</p>'
new_faq = '<p>Up to 60 day guests. For overnight stays, up to 34 adults can stay at Orchid Tree across its 11 rooms. Additional accommodation can bring the combined Orchid Tree + Viva Farm capacity to approximately 60 guests, by arrangement and subject to rooming and availability.</p>'
c = c.replace(old_faq, new_faq)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
