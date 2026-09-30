import os
import re

exact_new = "Children aged 0–8 can be selected during booking. Children aged 7–8 may incur an additional charge depending on the room and bedding arrangement. Any applicable charge will be shown before booking confirmation."

filepath = 'shared/content.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'Couple Rooms sleep 2 adults.*?applicable charges\.', 'Couple Rooms accommodate 2 adults + 1 child (up to 8). ' + exact_new, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)


filepath = 'guest.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'Rooms sleep to their set count.*?applicable charges\.', 'Rooms sleep to their set count. ' + exact_new, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

