import os
import glob

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in {filepath}: {old_text[:30]}...")

# RED 1: Age logic
html_files = glob.glob('*.html')
for f in html_files:
    replace_in_file(f, "Adults</span><span class=\"bb-pop-sub\">Over 6</span>", "Adults</span><span class=\"bb-pop-sub\">9+</span>")
    replace_in_file(f, "Adults</span><span class=\"rc-sub\">Over 6</span>", "Adults</span><span class=\"rc-sub\">9+</span>")
    replace_in_file(f, "Children</span><span class=\"bb-pop-sub\">Age up to 8</span>", "Children</span><span class=\"bb-pop-sub\">0-8 years</span>")
    replace_in_file(f, "Children</span><span class=\"rc-sub\">Age up to 8</span>", "Children</span><span class=\"rc-sub\">0-8 years</span>")
    replace_in_file(f, "Children</span><span class=\"bb-pop-sub\">Age up to 6</span>", "Children</span><span class=\"bb-pop-sub\">0-8 years</span>")
    replace_in_file(f, "Children</span><span class=\"rc-sub\">Age up to 6</span>", "Children</span><span class=\"rc-sub\">0-8 years</span>")
    
    replace_in_file(f, "Adults</span><span class=\"bke-ss\">Over 6</span>", "Adults</span><span class=\"bke-ss\">9+</span>")
    replace_in_file(f, "Children</span><span class=\"bke-ss\">Age up to 6</span>", "Children</span><span class=\"bke-ss\">0-8 years</span>")
    replace_in_file(f, "Children</span><span class=\"bke-ss\">Age up to 8</span>", "Children</span><span class=\"bke-ss\">0-8 years</span>")
    
    # RED 2: Chandana capacity
    replace_in_file(f, "Sleeps up to 8</span>", "Sleeps up to 6 guests</span>")
    
    # RED 3: Meals
    replace_in_file(f, "Breakfast is on us. Dinner is to order.", "All three meals are included with every stay — breakfast, lunch and dinner. Meals are freshly prepared and served plated, with vegetarian and non-vegetarian options. Meal preferences and dietary requirements can be shared before arrival.")
    replace_in_file(f, "Breakfast, included", "Breakfast, lunch and dinner included")
    replace_in_file(f, "Lunch and dinner are pre-ordered from the restaurant.", "Meals are prepared to order and planned around your preferences.")
    
    # RED 4: Restaurant removal from Experiences
    replace_in_file(f, "See the restaurant and menu &rarr;", "Explore our dining experience")
    replace_in_file(f, "href=\"restaurant.html\"", "href=\"#\"") # Will clean up carefully below
    replace_in_file(f, "Read more about the table on the restaurant page", "Freshly prepared North Indian and Nepali meals are served plated and planned around your preferences.")

    # ORANGE 1: Pet Policy
    replace_in_file(f, "Orchid Tree is proudly pet-friendly across our expansive grounds, cottages, and family rooms.", "Pets are welcome in our Family Rooms and garden cottages. The Couple Rooms by the Pool are pet-free. Please carry your pet's valid vaccination certificate for check-in.")
    
    # RED 7: Buyout wording
    replace_in_file(f, "The estate is a full buyout, so it is only ever your gathering on the grounds.", "Your wedding includes exclusive use of the Orchid Tree estate. Accommodation for up to approximately 60 resident guests can be arranged across Orchid Tree and associated Viva Farm accommodation, subject to rooming and availability.")
    
    # ORANGE 2: Inclusion Block
    replace_in_file(f, "Breakfast, lunch and dinner come with every stay, cooked fresh and planned around your preferences. We ask for meal choices before arrival so the kitchen cooks for your table, not a buffet line. Vegetarian and non-vegetarian options are available, with dietary needs planned in advance. Every meal is served fresh, never held under a lamp.", "Breakfast, lunch and dinner, high tea, millet snacks, tea, coffee and water, one full-body massage per room per night, a 15-minute Kansa foot massage for every guest, and full estate access.")

# Specific fix for Experiences restaurant link
with open('experiences.html', 'r', encoding='utf-8') as f:
    content = f.read()
if '<a href="restaurant.html">Explore our dining experience</a>' in content or '<a href="#">Explore our dining experience</a>' in content:
    content = content.replace('<a href="#">Explore our dining experience</a>', '<span style="color:var(--green);font-weight:600;">Explore our dining experience</span>')
    with open('experiences.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
