import os

filepath = 'shared/content.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('wellness band - massage is an optional add-on, pre-booked like meals.', 'wellness band - massage is included.')
text = text.replace('a massage can be added whenever you like', '1 full-body massage per room per night + 1 15-minute Kansa foot massage for every guest')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

