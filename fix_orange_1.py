import os

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '<p>Up to 60 day guests. Orchid Tree can accommodate up to 34 guests overnight.</p>',
    '<p>Corporate/private gatherings: up to 60 day guests.<br>Weddings: up to 200 celebration guests.<br>Overnight accommodation at Orchid Tree: up to 34 guests.</p>'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
