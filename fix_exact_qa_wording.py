import os

f1 = 'host-with-us.html'
with open(f1, 'r', encoding='utf-8') as file:
    c1 = file.read()

c1 = c1.replace(
    '<div class="lbl">Overnight guests at Orchid Tree, up to</div>',
    '<div class="lbl">Overnight guests, up to</div>'
)
c1 = c1.replace(
    '<div class="lbl">Overnight guests</div>',
    '<div class="lbl">Overnight accommodation for guests</div>'
)

with open(f1, 'w', encoding='utf-8') as file:
    file.write(c1)
