import os

# RED-01 & RED-02: blog-intimate-wedding-venues-near-bangalore.html
f1 = 'blog-intimate-wedding-venues-near-bangalore.html'
with open(f1, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '''<p>The estate is proudly BYOB. You choose the wine, the whisky, the champagne for the toast. The bar is yours, poured by your people, at the pace you set. There is no pressure, no corkage theatre, and no list of approved vendors for the bottle. The details are worth reading before the planning conversations begin.</p>''',
    '''<p>Orchid Tree follows a BYOB approach, subject to applicable event permissions. Alcohol is not included in the wedding package. If the family wishes to serve alcohol, the required temporary excise permission must be obtained, and applicable government charges are extra. Please discuss the arrangements with our event team during planning.</p>'''
)

c = c.replace(
    '''The estate holds eleven rooms onsite, comfortably accommodating around sixty resident guests through associated stay arrangements. For the ceremony and celebration itself, the estate can welcome up to two hundred guests across the day''',
    '''Orchid Tree has 11 onsite rooms accommodating up to 34 adults overnight. Additional accommodation for up to approximately 60 resident guests in total can be arranged through associated Viva Farm accommodation, subject to rooming and availability.</p>\n\n      <p>The estate can host wedding celebrations for up to 200 guests, with overnight accommodation planned separately'''
)

c = c.replace(
    '''Up to around sixty guests can stay overnight through associated arrangements across the eleven rooms. For the ceremony and celebration itself, the estate can welcome up to two hundred guests across the day.''',
    '''Up to 34 adults can stay overnight at Orchid Tree's 11 rooms. Additional accommodation for up to approximately 60 resident guests in total can be arranged through associated Viva Farm accommodation, subject to rooming and availability. For the ceremony and celebration itself, the estate can welcome up to two hundred guests across the day.'''
)

c = c.replace(
    '''The estate is BYOB, so you choose and bring your own drinks. There is no corkage fee and no approved vendor list for bottles.''',
    '''Orchid Tree follows a BYOB approach, subject to applicable event permissions. Alcohol is not included in the wedding package. If the family wishes to serve alcohol, the required temporary excise permission must be obtained, and applicable government charges are extra.'''
)

with open(f1, 'w', encoding='utf-8') as file:
    file.write(c)


# ORANGE-01: plan-your-dining.html
f2 = 'plan-your-dining.html'
with open(f2, 'r', encoding='utf-8') as file:
    c2 = file.read()

c2 = c2.replace('<a class="back-link" href="#">', '<a class="back-link" href="blog-farm-to-table-dining-near-bangalore.html">')

with open(f2, 'w', encoding='utf-8') as file:
    file.write(c2)


# ORANGE-03: blog-farm-to-table-dining-near-bangalore.html
f3 = 'blog-farm-to-table-dining-near-bangalore.html'
with open(f3, 'r', encoding='utf-8') as file:
    c3 = file.read()

c3 = c3.replace(
    '''<p>Every stay also includes high tea and snacks, one full-body massage per room per night, a 15-minute Kansa foot massage for every guest, and full estate access.</p>''',
    '''<p>Every overnight stay includes breakfast, lunch, dinner, high tea and millet snacks, along with one full-body massage per room per night and a 15-minute Kansa foot massage for every guest.</p>'''
)
c3 = c3.replace(
    '''breakfast, lunch, dinner, high tea and snacks''',
    '''breakfast, lunch, dinner, high tea and millet snacks'''
)

with open(f3, 'w', encoding='utf-8') as file:
    file.write(c3)


# BLUE-01: faq.html
f4 = 'faq.html'
with open(f4, 'r', encoding='utf-8') as file:
    c4 = file.read()

c4 = c4.replace(
    '''Yes. The Family Rooms and Chandana, the family cottage, are made for families and groups, with flexible bedding for children eight and under.''',
    '''Yes. The Family Rooms and Chandana, the family cottage, are made for families and groups. Adults are guests aged 9 years and above. Children are guests aged 0–8 years. Children aged 7–8 may incur an additional charge depending on the room and bedding arrangement. Any applicable charge will be shown before booking confirmation.'''
)

with open(f4, 'w', encoding='utf-8') as file:
    file.write(c4)
