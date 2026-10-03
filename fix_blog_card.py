import os

f = 'blog.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    'A private forest estate, up to sixty guests, calm over crowds.',
    'A private forest estate for celebrations of up to 200 guests, with accommodation for up to 60 resident guests.'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
