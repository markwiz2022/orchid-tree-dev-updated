import os

f = 'api/create-booking.js'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    'const { checkin, checkout, adults, children, guestName, guestPhone, guestEmail, roomIds, subtotal } = req.body;',
    '''const { checkin, checkout, adults, children, guestName, guestPhone, guestEmail, roomIds, subtotal } = req.body;

  const totalGuests = (parseInt(adults) || 0) + (parseInt(children) || 0);
  if (totalGuests > 34) {
    return res.status(400).json({ error: 'Orchid Tree accommodates a maximum of 34 overnight guests.' });
  }'''
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)