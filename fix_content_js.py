import os

file_path = 'shared/content.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '"615+ Google reviews"',
        '"670+ Google reviews"'
    ),
    (
        '"4.4 from 615+ guests"',
        '"4.4 from 670+ Google reviews"'
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
