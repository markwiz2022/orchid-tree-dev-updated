import os
import re

def rep(filepath, old, new, is_regex=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    if is_regex:
        new_c = re.sub(old, new, c, flags=re.DOTALL)
    else:
        new_c = c.replace(old, new)
    if new_c != c:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Replaced in {filepath}")

# RED 01 - plan-your-dining.html
f = 'plan-your-dining.html'
rep(f, 'Your reservation', 'Plan your meals')
rep(f, 'Booking confirmed', 'Already booked your stay? Tell our kitchen what you would like us to prepare.')
rep(f, 'Prices are indicative. The final bill is settled at the property. Subject to availability on the day.', 'Your stay includes breakfast, lunch, dinner, high tea and snacks. Any separately priced beverages or celebration add-ons will be clearly identified before you confirm them.')
rep(f, 'Prices are indicative. The final bill is settled at the property.', 'Your stay includes breakfast, lunch, dinner, high tea and snacks. Any separately priced beverages or celebration add-ons will be clearly identified before you confirm them.')

# RED 02 - corporate.html
f = 'corporate.html'
rep(f, 'Remove friction', 'Plan your event')
rep(f, 'Tell us just enough for a real conversation. No long questionnaire, no budget field on the first touch. We reply by hand, usually within a day.', 'Tell us your preferred dates, group size and what you are planning. We will come back with the right format and next steps, usually within a day.')
rep(f, 'This is an enquiry, not a booking. No budget field on the first touch. We read every one and reply by hand.', '')

# RED 03 - weddings.html
f = 'weddings.html'
rep(f, 'The numbers sit here, before the FAQ, so the right client feels reassured and the wrong enquiry never begins.', '')
rep(f, 'The numbers, quietly', 'The numbers, at a glance')
# We need to replace the section text for the numbers. Let's see exactly what's there first.
