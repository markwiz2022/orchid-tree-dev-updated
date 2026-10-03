import re

f = 'guest.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('cur = { name:name, email:email, phone:phone };', '')
c = c.replace('step(2);', '''
          booking = S.update(booking.id, { guest: { name: name, email: email, phone: pretty(phone), whatsapp: pretty(phone), phoneVerified: true } });
          renderGuestBlock();
          renderCtas();
''')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)