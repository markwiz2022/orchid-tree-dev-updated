import os

f = 'faq.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('Family Rooms sleep up to four; and Chandana, the family cottage, sleeps up to six.', 'Family Rooms sleep up to 4 (any mix of adults & children); and Chandana, the family cottage, sleeps up to 6 (any mix of adults & children).')
c = c.replace('Chandana, the Family Garden Cottage, sleeps up to six', 'Chandana, the Family Garden Cottage, sleeps up to 6 (any mix of adults & children)')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
