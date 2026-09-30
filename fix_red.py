import os
import glob

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in {filepath}")

# RED 1
replace_in_file('home.html', 'Children up to age 6 stay on existing bedding.', 'Children aged 0–8 can be selected during booking. Children aged 7–8 may require additional charges.')
replace_in_file('index.html', 'Children up to age 6 stay on existing bedding.', 'Children aged 0–8 can be selected during booking. Children aged 7–8 may require additional charges.')
replace_in_file('guest.html', 'Children up to age 6 share existing bedding.', 'Children aged 0–8 share existing bedding. Ages 7-8 may incur applicable charges.')
replace_in_file('stays.html', '(to 6)', '(to 8)')
replace_in_file('experiences.html', 'flexible bedding for children eight and under', 'flexible bedding for children 0–8 years')
replace_in_file('shared/content.js', 'Couple Rooms sleep 2 adults + 1 child up to 8 years, on one queen bed. No extra bed.', 'Couple Rooms sleep 2 adults + 1 child up to 8 years on existing bedding. Children aged 7–8 may incur applicable charges.')

# RED 2
replace_in_file('host-with-us.html', 'Breakfast is included with overnight stays, lunch and dinner are planned with you', 'For overnight event guests, breakfast, lunch and dinner are included, with menus planned around the event and dietary requirements')
replace_in_file('host-with-us.html', 'Breakfast is included with overnight stays. Lunch and dinner are plated, farm-to-table and customised with you', 'For overnight event guests, breakfast, lunch and dinner are included, with menus planned around the event and dietary requirements')

# RED 3 (Restaurant Links)
replace_in_file('experiences.html', 'Explore our dining experience', 'Read about dining at Orchid Tree')
replace_in_file('blog-weekend-getaways-near-bangalore.html', 'There is more on the <a href="restaurant.html">restaurant page</a>', 'There is more on the <a href="stays.html">stays page</a>')
replace_in_file('blog-farm-to-table-dining-near-bangalore.html', 'See the restaurant', 'Read about dining at Orchid Tree')

# RED 4
replace_in_file('corporate.html', 'Depending on the programme, bookings may reserve specific event spaces or the full estate. Your proposal will state the exact exclusivity included.', 'Corporate programmes can be booked as specific event-space reservations or as an exclusive full-estate buyout. Your proposal will clearly state the level of exclusivity included.')

# ORANGE 1
replace_in_file('stays.html', 'Breakfast, lunch and dinner are included, cooked fresh and served warm. Share your preferences and dietary needs before arrival.', 'Breakfast, lunch and dinner, high tea and snacks are included with every stay.')

# ORANGE 2
replace_in_file('stays.html', 'One full-body massage per room per night. A massage, whenever you like.', 'One full-body massage per room per night, scheduled at a time convenient for you.')

# ORANGE 3
replace_in_file('weddings.html', 'intimate celebrations of up to 200 guests, with accommodation for up to 60.', 'intimate celebrations of up to 200 guests, with accommodation for up to 60 across Orchid Tree and associated Viva Farm accommodation.')

# ORANGE 4
replace_in_file('corporate.html', '11 rooms onsite; larger residential groups only by associated arrangement', '11 rooms onsite · up to 34 overnight guests at Orchid Tree · larger residential groups by associated arrangement')

# BLUE 1
replace_in_file('blog-farm-to-table-dining-near-bangalore.html', 'It is a constraint that produces better food. It is a constraint that produces better food.', 'It is a constraint that produces better food.')

# BLUE 2
replace_in_file('blog-farm-to-table-dining-near-bangalore.html', 'You can read more about, and see how the kitchen is set up before you arrive.', 'You can read more about the dining experience and see how the kitchen works before you arrive.')

# BLUE 3
replace_in_file('blog-intimate-wedding-venues-near-bangalore.html', 'The details of are worth reading before the planning conversations begin.', 'The details are worth reading before the planning conversations begin.')

# BLUE 4
replace_in_file('blog-intimate-wedding-venues-near-bangalore.html', 'Sixty people, a forest, and a sky with no ceiling', 'A private estate, a forest, and a sky with no ceiling')

