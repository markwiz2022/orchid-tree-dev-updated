import os

f1 = 'host-with-us.html'
with open(f1, 'r', encoding='utf-8') as file:
    c1 = file.read()

c1 = c1.replace(
    '<div class="lbl">Adults overnight at Orchid Tree, up to</div>',
    '<div class="lbl">Overnight guests at Orchid Tree, up to</div>'
)
c1 = c1.replace(
    '<div class="lbl">Overnight accommodation for adults</div>',
    '<div class="lbl">Overnight guests</div>'
)

with open(f1, 'w', encoding='utf-8') as file:
    file.write(c1)

f2 = 'blog-intimate-wedding-venues-near-bangalore.html'
with open(f2, 'r', encoding='utf-8') as file:
    c2 = file.read()

c2 = c2.replace(
    'Orchid Tree accommodates up to 34 guests overnight.</p>',
    'Orchid Tree accommodates up to 34 guests overnight, subject to room-specific occupancy limits.</p>'
)

with open(f2, 'w', encoding='utf-8') as file:
    file.write(c2)
