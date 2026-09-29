import os

file_path = 'stays.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "and for two days, every one of them is yours.",
        "and for a night or weekend, the estate is yours."
    ),
    (
        "<h3>Breakfast, included</h3><p>Cooked fresh each morning and plated, never a buffet. Lunch and dinner are pre-ordered from the restaurant.</p>",
        "<h3>Included: meals</h3><p>Breakfast, lunch and dinner are included, cooked fresh and served warm. Share your preferences and dietary needs before arrival.</p>"
    ),
    (
        '''<h3>Proudly BYOB</h3><p>Bring your own bottle and pour it slowly in the outdoor lounge, under the stars when the bonfire catches.</p>''',
        '''<h3>Wellness, included</h3><p>One full-body massage per room per night, plus a 15-minute Kansa foot massage for every guest.</p>'''
    ),
    (
        "Mary was a wonderful host",
        "Meena was a wonderful host"
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
