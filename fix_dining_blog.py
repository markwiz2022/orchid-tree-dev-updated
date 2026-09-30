import os

f = 'blog-farm-to-table-dining-near-bangalore.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('We ask you to pre-order in advance before the kitchen begins.', 'Meal preferences are collected before arrival so the kitchen can prepare for your stay.')
c = c.replace('Pre-ordering works best when you have arrived and had time to settle. ', '')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

