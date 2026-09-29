import os

file_path = 'about.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "615+ guests",
        "670+ Google reviews"
    ),
    (
        "We share the exact location once your stay is confirmed, for privacy.",
        "Directions and arrival instructions are shared with your booking confirmation."
    ),
    (
        "reservations@orchidtree.in",
        "orchidtree.blr@gmail.com"
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
