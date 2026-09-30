import os

filepath = 'blog-weekend-getaways-near-bangalore.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('There is more on the <a href="#">restaurant page</a> if you like to plan your meals before you arrive.', 'There is more on the <a href="experiences.html">dining section</a> if you like to read about how meals work.')
text = text.replace('There is more on the <a href="restaurant.html">restaurant page</a> if you like to plan your meals before you arrive.', 'There is more on the <a href="experiences.html">dining section</a> if you like to read about how meals work.')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

