import os
import glob
import re

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in {filepath}: {old_text[:30]}")

def regex_replace_in_file(filepath, pattern, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(pattern, new_text, content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Regex replaced in {filepath}: {pattern}")


# RED 1 - Stays room cards (child to 6 -> up to 8)
# Wait, I already did this to (to 8). Let's fix to (up to 8)
regex_replace_in_file('stays.html', r'\(to 8\)', '(up to 8)')
regex_replace_in_file('stays.html', r'\(to 6\)', '(up to 8)')

# RED 1 - Booking note
bedding_old_1 = r"Children aged 0-8 can be selected during booking. Children aged 7-8 may require additional charges."
bedding_old_2 = r"Children up to age 6 stay on existing bedding."
bedding_new = "Children aged 0–8 can be included in the booking. Children aged 0–6 may use existing bedding; additional bedding for older children is subject to availability and applicable charges."
regex_replace_in_file('home.html', bedding_old_1, bedding_new)
regex_replace_in_file('index.html', bedding_old_1, bedding_new)
regex_replace_in_file('home.html', bedding_old_2, bedding_new)
regex_replace_in_file('index.html', bedding_old_2, bedding_new)
regex_replace_in_file('orchidtree-home-wireframe.html', bedding_old_2, bedding_new)

# Guest/Content JS
regex_replace_in_file('guest.html', r"Children aged 0-8 share existing bedding. Ages 7-8 may incur applicable charges.", bedding_new)
regex_replace_in_file('shared/content.js', r"Couple Rooms sleep 2 adults \+ 1 child up to 8 years on existing bedding. Children aged 7-8 may incur applicable charges.", "Couple Rooms accommodate 2 adults + 1 child up to 8 years. Children aged 0-6 share existing bedding. Ages 7-8 may incur applicable charges for additional bedding.")

# ORANGE 1
# Remove 'A massage, whenever you like.' if it still exists anywhere, or 'One full-body massage per room per night, scheduled at a time convenient for you.'
# The audit wants 'Your included full-body massage can be scheduled at a time convenient for you.'
replace_in_file('stays.html', 'One full-body massage per room per night, scheduled at a time convenient for you.', 'Your included full-body massage can be scheduled at a time convenient for you.')
replace_in_file('stays.html', 'A massage, whenever you like.', 'Your included full-body massage can be scheduled at a time convenient for you.')

# ORANGE 2
# Stays inclusions - replace the heading/copy with:
# "Breakfast, lunch and dinner, high tea and snacks are included with every stay."
replace_in_file('stays.html', '<h3>Included: meals</h3><p>Breakfast, lunch and dinner, high tea and snacks are included with every stay.</p>', '<h3>Breakfast, lunch and dinner, high tea and snacks</h3><p>Breakfast, lunch and dinner, high tea and snacks are included with every stay.</p>')

# ORANGE 3
replace_in_file('faq.html', 'You get full hospitality (breakfast, a restaurant, pool, steam room and activities)', 'You get full hospitality — breakfast, lunch and dinner prepared by our kitchen, plus the pool, steam room and activities —')

# ORANGE 4
# Corporate headline. "60 day guests · up to 34 overnight at Orchid Tree · up to approximately 60 with Viva Farm by arrangement"
replace_in_file('corporate.html', '<span><b>11</b> rooms onsite; larger residential groups only by associated arrangement</span>', '<span>60 day guests &middot; up to 34 overnight at Orchid Tree &middot; up to approximately 60 with Viva Farm by arrangement</span>')

