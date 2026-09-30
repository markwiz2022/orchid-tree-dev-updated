import os
import re

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_stats = '''      <div class="stat">
        <div class="num">11</div>
        <div class="lbl">Rooms, one estate</div>
      </div>
      <div class="stat">
        <div class="num">60</div>
        <div class="lbl">Day guests, up to</div>
      </div>
      <div class="stat">
        <div class="num">34</div>
        <div class="lbl">Overnight, up to</div>
      </div>'''

new_stats = '''      <div class="stat">
        <div class="num">60</div>
        <div class="lbl">Day guests, up to</div>
      </div>
      <div class="stat" style="max-width: 250px;">
        <div class="num">34</div>
        <div class="lbl">Overnight at Orchid Tree, up to</div>
      </div>
      <div class="stat" style="max-width: 250px;">
        <div class="num">~60</div>
        <div class="lbl">Overnight across Orchid Tree + Viva Farm by arrangement</div>
      </div>'''

c = c.replace(old_stats, new_stats)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

