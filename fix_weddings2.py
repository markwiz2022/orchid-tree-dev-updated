import os
import re

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = re.sub(
    r'<div class="k">Day 1 [^<]+ Noon</div><h3>Arrive</h3><p>Rooming, welcome refreshments, lunch and an unhurried afternoon on the estate.</p>',
    '<div class="k">Day 1 &middot; Noon</div><h3>Arrive</h3><p>Wedding guests arrive from noon for welcome refreshments, lunch and the planned wedding programme. Room access follows the agreed event rooming schedule.</p><p style="margin-top:12px; font-size:13px; opacity:0.8;">Standard leisure-stay check-in is from 2 PM. Wedding and event arrival times are planned separately with the event team.</p>',
    c
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

