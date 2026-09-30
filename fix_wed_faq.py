import os

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old = '<p>Up to around 60 resident guests across Orchid Tree and the associated Viva Farm stay arrangement, subject to rooming. Additional hotel rooms nearby can be coordinated separately.</p>'
new = '<p>Up to 34 guests can stay at Orchid Tree itself, with additional accommodation at Viva Farm bringing the combined resident capacity to approximately 60 guests, subject to rooming and availability. Additional hotel rooms nearby can be coordinated separately.</p>'

c = c.replace(old, new)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

