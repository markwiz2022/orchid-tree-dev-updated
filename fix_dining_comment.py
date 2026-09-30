import os

f = 'plan-your-dining.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('STEP 1: BOOKING CONFIRMED', 'STEP 1: PLAN YOUR MEALS')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

