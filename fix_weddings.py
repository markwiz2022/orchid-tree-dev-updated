import os

file_path = 'weddings.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '<div class="big" data-count="200">0</div>',
        '<div class="big" data-count="200">200</div>'
    ),
    (
        '<div class="big" data-count="60">0</div>',
        '<div class="big" data-count="60">60</div>'
    ),
    (
        '<div class="big" data-count="45">0</div>',
        '<div class="big" data-count="45">45</div>'
    ),
    (
        '<div class="big" data-count="15">0</div>',
        '<div class="big" data-count="15">15</div>'
    ),
    (
        "organic and locally sourced food",
        "seasonal and locally sourced food"
    ),
    (
        ", the, or read more",
        ", or read more"
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
