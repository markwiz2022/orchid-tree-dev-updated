import os

filepath = 'stays.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<p class="incl-foot reveal">A massage, whenever you like.</p>', '<p class="incl-foot reveal">One full-body massage per room per night, scheduled at a time convenient for you.</p>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

