import os

f = 'faq.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('<p>Yes, breakfast is included with every stay.</p>', '<p>Yes. Overnight stays include breakfast, lunch, dinner, high tea and snacks, together with the wellness inclusions and estate access stated at the time of booking.</p>')
c = c.replace('breakfast, lunch and dinner prepared by our kitchen', 'breakfast, lunch, dinner, high tea and snacks prepared by our kitchen')
c = c.replace('all three meals are included', 'breakfast, lunch, dinner, high tea and snacks are included')
c = c.replace('all three meals', 'breakfast, lunch, dinner, high tea and snacks')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

