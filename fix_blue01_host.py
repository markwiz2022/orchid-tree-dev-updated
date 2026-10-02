import os

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Replace the "proudly BYOB." text in host-with-us.html
c = c.replace('and we are proudly BYOB.', 'Orchid Tree follows a BYOB approach for events, subject to applicable permissions and event arrangements. Alcohol is not included in the event package. Any required permissions and applicable government charges are the responsibility of the organiser. Please discuss the arrangements with our event team during planning.')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)