import os

f = 'faq.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('Your room, breakfast, lunch, dinner, high tea and snacks, high tea, snacks and full estate access are included.', 'Your room, breakfast, lunch, dinner, high tea and snacks, and full estate access are included.')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

