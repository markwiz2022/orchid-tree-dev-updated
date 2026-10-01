import os

f = 'blog-farm-to-table-dining-near-bangalore.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_p = '<p>Breakfast, lunch and dinner are included with every stay and served fresh. All three meals are plated and cooked in small batches to order. Meal preferences are collected before arrival so the kitchen can prepare for your stay. There is no buffet, no warming tray, no food that has been sitting under a lamp since two in the afternoon. When your meal arrives, it was cooked for you, not for a queue.</p>'

new_p = old_p + '\n\n      <p>Every stay also includes high tea and snacks, one full-body massage per room per night, a 15-minute Kansa foot massage for every guest, and full estate access.</p>'

c = c.replace(old_p, new_p)

# Also let's update the FAQ in that article:
old_faq = '<p>Yes. Breakfast, lunch and dinner are included with every stay. Every meal is cooked to order and brought to your table, not waiting in a warming tray. We ask for meal choices before arrival so the kitchen cooks for your table.</p>'
new_faq = '<p>Yes. Overnight stays include breakfast, lunch, dinner, high tea and snacks. Every meal is cooked to order and brought to your table, not waiting in a warming tray. We ask for meal choices before arrival so the kitchen cooks for your table.</p>'
c = c.replace(old_faq, new_faq)


with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

