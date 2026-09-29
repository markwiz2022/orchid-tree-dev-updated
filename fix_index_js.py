import os
import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract INCLUDED section
included_regex = r"(<!-- INCLUDED -->\s*<section class=\"incl\" id=\"included\">.*?</section>\s*)"
included_match = re.search(included_regex, content, re.DOTALL)

if included_match:
    included_block = included_match.group(1)
    # Remove it from its original place
    content = content.replace(included_block, "")
    # Insert it right before <!-- ROOMS -->
    content = content.replace("<!-- ROOMS -->", included_block + "\n  <!-- ROOMS -->")
    print("Moved INCLUDED section in index.html")
else:
    print("INCLUDED section not found!")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update shared/content.js
js_path = 'shared/content.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

old_js_with = "Your rate covers the room, breakfast each morning, and the run of the estate: pool, steam room, snacks, games, and fresh linens. Includes 1 full body massage per room per night + veg and non-veg variants for all meals (Lunch, High-tea, Dinner and Breakfast) and 15 mins Kansa foot massage for all guests. Lunch, dinner, and a massage can be pre-booked separately, and your food credit goes toward your meals."
new_js_with = "Your stay includes all three meals, high tea and snacks, plus one full-body massage per room per night. Every guest also receives a 15-minute Kansa foot massage. You'll have full access to the estate throughout your stay, including the landscaped gardens, ozone pool, steam room, indoor games, open spaces and fresh linens. Vegetarian and non-vegetarian meal options are available."

old_js_without = "Your rate covers the room, breakfast each morning, and the run of the estate: pool, steam room, snacks, games, and fresh linens. Includes 1 full body massage per room per night + veg and non-veg variants for all meals (Lunch, High-tea, Dinner and Breakfast) and 15 mins Kansa foot massage for all guests. Lunch, dinner, and a massage can be pre-booked separately."
new_js_without = "Your stay includes all three meals, high tea and snacks, plus one full-body massage per room per night. Every guest also receives a 15-minute Kansa foot massage. You'll have full access to the estate throughout your stay, including the landscaped gardens, ozone pool, steam room, indoor games, open spaces and fresh linens. Vegetarian and non-vegetarian meal options are available."

js_content = js_content.replace(old_js_with, new_js_with)
js_content = js_content.replace(old_js_without, new_js_without)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated shared/content.js")

