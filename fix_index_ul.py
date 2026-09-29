import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_ul = '''            <ul>
              <li>Three farm-to-fork organic meals</li>
              <li>In-room pantry with ragi &amp; millet snacks, teas and coffees</li>
              <li>Kansa foot massage + head massage for every guest</li>
              <li>Ozone pool, steam room &amp; full estate access</li>
              <li>Fresh linen, enzyme-washed in-house</li>
            </ul>'''

new_ul = '''            <ul>
              <li>All three freshly prepared meals + high tea</li>
              <li>Millet snacks, tea, coffee and water</li>
              <li>1 full-body massage per room per night + Kansa foot massage for every guest</li>
              <li>Ozone pool, steam room, games and full estate access</li>
              <li>Fresh linen, enzyme-washed in-house</li>
            </ul>'''

if old_ul in content:
    content = content.replace(old_ul, new_ul)
    print("Replaced inclusions UL list.")
else:
    print("Inclusions UL list NOT FOUND!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
