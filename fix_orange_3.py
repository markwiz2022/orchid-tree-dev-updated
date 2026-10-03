import os

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '<p class="muted" style="margin-top:16px;max-width:720px;">Up to 200 celebration guests, with overnight accommodation for up to 34 guests at Orchid Tree.</p>',
    '<p class="muted" style="margin-top:16px;max-width:720px;">Up to 200 celebration guests, with overnight accommodation for up to 34 guests at Orchid Tree. Every wedding is a full-estate buyout. No other overnight guests are on the property during your celebration.</p>'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
