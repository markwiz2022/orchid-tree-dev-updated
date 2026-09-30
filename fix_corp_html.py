import os
import re

f = 'corporate.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

bad_block = '''      <div class="hero-stats" style="color:rgba(255,255,255,0.9); font-size:15px; letter-spacing:0.5px; font-weight:500; text-align:center;">60 day guests &middot; up to 34 overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement</div>
        <div class="s"><span class="big" data-count="60">60</span><span class="lbl">day guests</span></div>
        <div class="s"><span class="big" data-count="11">11</span><span class="lbl">rooms onsite</span></div>
        <div class="s"><span class="big">One</span><span class="lbl">team at a time</span></div>
      </div>'''

good_block = '''      <div class="hero-stats" style="display:block; color:rgba(255,255,255,0.9); font-size:16px; letter-spacing:0.5px; font-weight:500; padding:12px 0;">
        60 day guests &middot; up to 34 overnight at Orchid Tree &middot; up to approx 60 with Viva Farm by arrangement
      </div>'''

c = c.replace(bad_block, good_block)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

