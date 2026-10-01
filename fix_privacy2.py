import os

f = 'privacy-policy.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Task 1
old_1 = 'Last updated June 2026. This is a template and the wording should be reviewed before launch.'
new_1 = 'Last updated: June 2026.'
c = c.replace(old_1, new_1)

# Task 2
old_2 = '<li>Breakfast is included with overnight stays. Lunch and dinner are plated, farm-to-table and pre-ordered. Orchid Tree is proudly BYOB.</li>'
new_2 = '<li>Stays: Overnight stays include breakfast, lunch, dinner, high tea and snacks, together with the wellness inclusions and estate access stated at the time of booking.</li>'
c = c.replace(old_2, new_2)

# Task 3
old_3 = '<li>An enquiry is not a confirmed booking. A booking is confirmed only once we agree the dates and any deposit in writing.</li>'
new_3 = '<li>Enquiries and bookings: An enquiry is not a confirmed booking. A leisure stay is confirmed once the booking details and the full amount shown at checkout have been successfully confirmed. Nothing is due on arrival unless explicitly stated in the booking confirmation. Event and full-estate bookings are confirmed separately in writing according to their agreed terms.</li>'
c = c.replace(old_3, new_3)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
