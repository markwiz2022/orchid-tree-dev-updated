import os

file_path = 'experiences.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "These come with the room. Breakfast every morning, the water, the steam, the games. Nothing here is an upsell.",
        "These come with the room: all three meals, wellness, the pool, steam, games and the estate. Nothing essential is an upsell."
    ),
    (
        "Breakfast comes with every stay. Lunch and dinner are a la carte from the restaurant, cooked fresh and pre-ordered before you arrive, so the kitchen cooks to your table, not to a buffet bin. Proudly BYOB. You will taste the difference of food made to order, not held warm under a lamp.",
        "Breakfast, lunch and dinner come with every stay, cooked fresh and planned around your preferences. We ask for meal choices before arrival so the kitchen cooks for your table, not a buffet line. Vegetarian and non-vegetarian options are available, with dietary needs planned in advance. Every meal is served fresh, never held under a lamp."
    ),
    (
        "Your room, breakfast each morning, and the run of the estate: the ozone pool, the steam room and open-sky showers, the millet snack station, indoor games, the open-air gym and the BYOB lounge. Lunch, dinner and a massage can be added separately.",
        "Your room, all three meals, high tea and snacks, plus the run of the estate: ozone pool, steam room, open-sky showers, indoor games and open-air gym. One full-body massage per room and a 15-minute Kansa foot massage for every guest are also included."
    ),
    (
        "Breakfast is included with every stay. Lunch and dinner are a la carte from the on-site restaurant, cooked fresh to order, so we ask you to pre-order before you arrive. Orchid Tree is proudly BYOB.",
        "Yes. Breakfast, lunch and dinner are included with every stay, cooked fresh to order with vegetarian and non-vegetarian choices. We ask for preferences and dietary needs before arrival so every meal is prepared for your table."
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
