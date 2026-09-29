import os

file_path = 'corporate.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        '<span class="big" data-count="45">0</span>',
        '<span class="big" data-count="45">45</span>'
    ),
    (
        '<span class="big" data-count="60">0</span>',
        '<span class="big" data-count="60">60</span>'
    ),
    (
        '<span class="big" data-count="11">0</span>',
        '<span class="big" data-count="11">11</span>'
    ),
    (
        "taken by one company at a time. No ballroom, no other event running beside yours.",
        "designed for focused leadership retreats and team offsites."
    ),
    (
        "<span><b>11</b> rooms onsite</span><span class=\"dia\">&#9670;</span>\n        <span>Up to <b>~60</b> combined stay with Viva Farm</span>",
        "<span><b>11</b> rooms onsite; larger residential groups only by associated arrangement</span>"
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
