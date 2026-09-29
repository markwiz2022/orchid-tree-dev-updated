import os

file_path = 'faq.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "Your room, breakfast each morning, and the run of the estate: the pool, steam room, snacks, indoor games and fresh linen. Lunch, dinner and a massage can be pre-booked separately.",
        "Your room, all three meals, high tea, snacks and full estate access are included. One full-body massage per room and a 15-minute Kansa foot massage for every guest are included too."
    ),
    (
        "Breakfast is included with every stay. Lunch and dinner are à la carte from the restaurant, cooked fresh to order, so we recommend pre-ordering before you arrive.",
        "Yes. Breakfast, lunch and dinner are included, cooked fresh to order. Tell us your preferences and dietary needs before arrival so the kitchen can plan every meal around your stay."
    ),
    (
        "Breakfast is included with every stay. Lunch and dinner are  la carte from the restaurant, cooked fresh to order, so we recommend pre-ordering before you arrive.",
        "Yes. Breakfast, lunch and dinner are included, cooked fresh to order. Tell us your preferences and dietary needs before arrival so the kitchen can plan every meal around your stay."
    ),
    (
        "There is a steam room for all guests, and a massage can be added to your stay whenever you like. The garden cottages have their own private steam rooms.",
        "The steam room is open to all guests. Every stay includes one full-body massage per room and a 15-minute Kansa foot massage for every guest. Garden cottages have private steam rooms."
    )
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:30]}...")
    else:
        print(f"NOT FOUND: {old[:30]}...")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
