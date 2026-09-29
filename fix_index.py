import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "615+ guests",
        "670+ Google reviews"
    ),
    (
        "615+ Google reviews",
        "670+ Google reviews"
    ),
    (
        "Some rooms sit by the pool, bright and easy, steps from the water. Others are cottages built into the trees, with baths open to the sky. Pick the feeling you're after. Every room comes with breakfast, the pool, the steam room, and the run of the estate. Each room is named after a tree on the estate.",
        "Some rooms sit by the pool, bright and easy, steps from the water. Others are cottages built into the trees, with baths open to the sky. Pick the feeling you're after. Every stay includes all three meals, wellness, and the run of the estate. Each room is named after a tree growing here."
    ),
    (
        "Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage.",
        "Your stay includes all three meals, high tea and snacks, plus one full-body massage per room. Every guest receives a 15-minute Kansa foot massage, with full estate access."
    ),
    (
        "Your room, breakfast, all estate activities, and amenities like the pool, steam room, and games. Lunch and dinner are served fresh at the restaurant and can be pre-ordered, and a massage can be added whenever you like.",
        "Your room, all three meals, high tea, snacks, and full estate access are included. You also receive one full-body massage per room per night, plus a 15-minute Kansa foot massage for every guest."
    ),
    (
        "Breakfast is included with every stay. Lunch and dinner are a la carte from our restaurant, cooked fresh to order, so we recommend pre-ordering before you arrive.",
        "Yes. Every stay includes breakfast, lunch and dinner, freshly prepared to your preferences, along with high tea, snacks, wellness and full estate access. Tell us dietary needs before you arrive."
    ),
    (
        "About forty-five minutes from Whitefield, in Bangalore Rural near Hoskote. The exact location is shared once your stay is confirmed, to keep the estate private.",
        "About forty-five minutes from Whitefield, in Bangalore Rural near Hoskote. Directions and arrival instructions are shared with your booking confirmation, so getting here is simple."
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
