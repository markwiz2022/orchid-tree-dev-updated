import os

file_path = 'host-with-us.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "Two spaces, indoor and open air &nbsp;·&nbsp; <b>Up to 60</b> day guests, <b>34</b> overnight &nbsp;·&nbsp; Calm over crowds, always",
        "45 min from Whitefield &nbsp;·&nbsp; 11 rooms onsite &nbsp;·&nbsp; Corporate/private gatherings up to 60 &nbsp;·&nbsp; Weddings up to 200"
    ),
    (
        "Two spaces, indoor and open air &nbsp;&nbsp; <b>Up to 60</b> day guests, <b>34</b> overnight &nbsp;&nbsp; Calm over crowds, always",
        "45 min from Whitefield &nbsp;&nbsp; 11 rooms onsite &nbsp;&nbsp; Corporate/private gatherings up to 60 &nbsp;&nbsp; Weddings up to 200"
    ),
    (
        "The Multi-Purpose Hall",
        "Gulmohar Hall"
    ),
    (
        "The Open Movement Stage",
        "Baobab Court"
    ),
    (
        "Multi-purpose hall",
        "Gulmohar Hall"
    ),
    (
        "multi-purpose AV hall",
        "Gulmohar AV Hall"
    ),
    (
        "an open movement stage",
        "Baobab Court"
    ),
    (
        "Bachelors party",
        "Private celebrations"
    ),
    (
        "bachelor parties",
        "private celebrations"
    ),
    (
        "Or look around the <a href=\"home.html#rooms\">estate and its rooms</a> and the.",
        "Or look around the <a href=\"index.html#rooms\">estate and its rooms</a>."
    ),
    (
        "yours to gather in",
        "ready to gather in"
    ),
    (
        "the whole estate yours for the day",
        "the estate as your private venue"
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
