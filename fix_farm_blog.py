import os

file_path = 'blog-farm-to-table-dining-near-bangalore.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "Breakfast is included with every stay and served fresh each morning. It is the meal that comes to you, and it is worth lingering over. Lunch and dinner are a different matter. Both are plated meals, cooked in small batches to order, and both are pre-ordered in advance, before the kitchen begins.",
        "Breakfast, lunch and dinner are included with every stay and served fresh. All three meals are plated and cooked in small batches to order. We ask you to pre-order in advance before the kitchen begins."
    ),
    (
        "Yes. Breakfast is included with every stay and served fresh each morning. It is cooked to order and comes to you, not waiting in a warming tray. Lunch and dinner are separate plated meals that you pre-order in advance.",
        "Yes. Breakfast, lunch and dinner are included with every stay. Every meal is cooked to order and brought to your table, not waiting in a warming tray. We ask for meal choices before arrival so the kitchen cooks for your table."
    ),
    (
        "Is breakfast included with a stay?",
        "Are meals included with a stay?"
    ),
    (
        "the tomatoes on your plate were probably pulled off the vine this morning, a kilometre down the road, on the estate's own farm. The gap between seed and table here is not a marketing claim. It is a walk you can take before lunch.",
        "the tomatoes on your plate were likely pulled off the vine this morning on the estate's own farm, supplemented by thoughtful local sourcing. The gap between seed and table here is not just a marketing claim. It is a walk you can take before lunch."
    ),
    (
        "There is no freezer full of backup produce, no sourcing from a wholesale market at four in the morning. What the farm offers that day is what the kitchen cooks with.",
        "The kitchen draws heavily on what the farm offers that day, supported by carefully selected local partners. It is a constraint that produces better food."
    ),
    (
        "The gap between seed and table here is not a marketing claim.",
        "The gap between seed and table here is not just a marketing claim."
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
