import os

f = 'privacy-policy.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Task 1
old_1 = 'Last updated June 2026. This is a template and the wording should be reviewed before launch.'
new_1 = 'Last updated: June 2026.'
c = c.replace(old_1, new_1)

# Task 2
old_2 = '<p>Breakfast is included with overnight stays.</p>'
new_2 = '<p>Stays: Overnight stays include breakfast, lunch, dinner, high tea and snacks, together with the wellness inclusions and estate access stated at the time of booking.</p>'
if old_2 not in c:
    # try just the text
    old_2_text = 'Breakfast is included with overnight stays.'
    new_2_text = 'Stays: Overnight stays include breakfast, lunch, dinner, high tea and snacks, together with the wellness inclusions and estate access stated at the time of booking.'
    c = c.replace(old_2_text, new_2_text)
else:
    c = c.replace(old_2, new_2)

# Task 3
# Find booking/payment wording.
# Wait, let's look at the actual text around booking.
