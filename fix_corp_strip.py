import os

f = 'corporate.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_strip = '''      <div class="model-band-facts reveal">
        <span>Up to <b>60</b> day guests</span><span class="dia">&#9670;</span>
        <span>60 day guests &middot; up to 34 overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement</span><span class="dia">&#9670;</span>
        <span><b>45</b> min from Whitefield</span>
      </div>'''

new_strip = '''      <div class="model-band-facts reveal">
        <span>Up to 60 day guests &middot; up to 34 adults overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement &middot; 45 min from Whitefield</span>
      </div>'''

c = c.replace(old_strip, new_strip)

# Also fix the hero stats at the top of corporate.html
old_hero = '60 day guests &middot; up to 34 overnight at Orchid Tree &middot; up to approx 60 with Viva Farm by arrangement'
new_hero = '60 day guests &middot; up to 34 adults overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement'
c = c.replace(old_hero, new_hero)

# Fix FAQ in corporate.html
old_faq = 'Yes. Orchid Tree accommodates up to 34 overnight guests across its 11 rooms.'
new_faq = 'Yes. Orchid Tree accommodates up to 34 adults overnight across its 11 rooms.'
c = c.replace(old_faq, new_faq)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

