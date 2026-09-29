import os

file_path = 'blog-weekend-getaways-near-bangalore.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "There is more on the if you like to plan your meals before you arrive.",
        "There is more on the <a href=\"restaurant.html\">restaurant page</a> if you like to plan your meals before you arrive."
    ),
    (
        "Whichever you choose, breakfast and the run of the estate come with it.",
        "Whichever you choose, all three meals, wellness and the run of the estate come with it."
    ),
    (
        "Food here is part of the rest, not a sideshow. Breakfast is included and cooked fresh. Lunch and dinner are plated and pre-ordered, North Indian and Nepali home cooking, much of it grown on the estate farm a kilometre away.",
        "Food here is part of the rest, not a sideshow. All three meals—breakfast, lunch and dinner—are included with every stay. They are plated, cooked fresh and planned around your preferences, featuring North Indian and Nepali home cooking, with seasonal produce from our farm."
    ),
    (
        "Your room, breakfast, the pool, the steam room, games, and all the activities across the estate. Lunch and dinner are plated and pre-ordered from the restaurant, and a massage can be added whenever you like.",
        "Your room, all three meals, high tea and snacks, plus one full-body massage per room and a 15-minute Kansa foot massage for every guest. You also get full estate access, including the pool and steam room."
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
