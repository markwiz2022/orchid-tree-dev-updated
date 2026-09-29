import os

file_path = 'blog-intimate-wedding-venues-near-bangalore.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "A private forest estate near Whitefield, full-estate buyout, up to 60 guests, plated farm-to-table menus.",
        "A private forest estate near Whitefield, full-estate buyout, up to 200 guests, plated farm-to-table menus."
    ),
    (
        "A private forest estate near Whitefield, available as a full buyout for up to 60 guests. Every intimate wedding at Orchid Tree is planned by hand.",
        "A private forest estate near Whitefield, available as a full buyout for up to 200 guests. Every intimate wedding at Orchid Tree is planned by hand."
    ),
    (
        "A private forest estate near Whitefield, full-estate buyout for up to 60 guests. Every wedding planned by hand.",
        "A private forest estate near Whitefield, full-estate buyout for up to 200 guests. Every wedding planned by hand."
    ),
    (
        "The estate holds eleven rooms across cottages and suites, comfortably accommodating up to thirty-four guests overnight. For the ceremony and celebration itself, the estate can welcome up to sixty guests across the day, which means your extended circle can join the rituals and the meal and still leave the intimacy intact for those who stay the night.",
        "The estate holds eleven rooms onsite, comfortably accommodating around sixty resident guests through associated stay arrangements. For the ceremony and celebration itself, the estate can welcome up to two hundred guests across the day, which means your extended circle can join the rituals and the meal and still leave the intimacy intact for those who stay the night."
    ),
    (
        "Up to thirty-four guests can stay overnight across the eleven rooms. For the ceremony and celebration itself, the estate can welcome up to sixty guests across the day.",
        "Up to around sixty guests can stay overnight through associated arrangements across the eleven rooms. For the ceremony and celebration itself, the estate can welcome up to two hundred guests across the day."
    ),
    (
        "https://images.unsplash.com/photo-1519741497674-611481863552?w=1100&q=80&auto=format&fit=crop",
        "images/uploads/wedding-ceremony-night-mandap.jpg"
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
