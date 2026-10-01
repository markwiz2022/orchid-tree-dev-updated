import os

f = 'stays.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_1 = 'Eleven rooms across a living forest, forty-five minutes from Whitefield. No two are the same, and for a night or weekend, the estate is yours.'
new_1 = 'Eleven rooms across a living forest, forty-five minutes from Whitefield. No two are the same, and for a night or weekend, the forest is your backdrop.'
c = c.replace(old_1, new_1)

old_2 = 'An estate kept small on purpose. No itinerary, no day visitors, no rush.'
new_2 = 'An estate kept small on purpose. No itinerary, no casual day visitors during normal stays, and no rush.'
c = c.replace(old_2, new_2)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

