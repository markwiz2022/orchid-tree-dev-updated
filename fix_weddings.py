import os

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Arrival 
old_arrival = '<div class="k">Day 1 &middot; Noon</div><h3>Arrive</h3><p>Rooming, welcome refreshments, lunch and an unhurried afternoon on the estate.</p>'
new_arrival = '<div class="k">Day 1 &middot; Noon</div><h3>Arrive</h3><p>Wedding guests arrive from noon for welcome refreshments, lunch and the planned wedding programme. Room access follows the agreed event rooming schedule.</p><p style="margin-top:12px; font-size:13px; opacity:0.8;">Standard leisure-stay check-in is from 2 PM. Wedding and event arrival times are planned separately with the event team.</p>'
c = c.replace(old_arrival, new_arrival)

# Capacity "34 adults" vs "34 guests"
old_stay = '<p>Up to 34 guests can stay across Orchid Tree\'s 11 rooms.'
new_stay = '<p>Up to 34 adults can stay across Orchid Tree\'s 11 rooms. Children may be accommodated within the room-specific child limits, subject to rooming and availability.'
c = c.replace(old_stay, new_stay)

# Also fix the FAQ in weddings
old_faq = 'Up to 34 guests can stay at Orchid Tree itself'
new_faq = 'Up to 34 adults can stay at Orchid Tree itself'
c = c.replace(old_faq, new_faq)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

