import os

f = 'guest.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_key = '6LfKp9MtAAAAADlEBlHphpcn7miDYH6Un0nu7rN'
new_key = '6LfKp9MtAAAAADILeBlHphpcn7miDYH6Un0nu7rN'
c = c.replace(old_key, new_key)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
