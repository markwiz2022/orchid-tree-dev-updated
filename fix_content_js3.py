import os

filepath = 'shared/content.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_str = '"Couple Rooms accommodate 2 adults + 1 child up to 8 years, sharing one American-standard queen bed.",'
new_str = '"Couple Rooms accommodate 2 adults + 1 child (up to 8). Children aged 7-8 may incur an additional charge depending on the room and bedding arrangement.",'

content = content.replace(old_str, new_str)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
