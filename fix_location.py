import os

file_path = 'shared/content.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "We share the exact location once your stay is confirmed, for privacy.",
        "Directions and arrival instructions are shared with your booking confirmation, so getting here is simple."
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
