import os

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('<h2>Come see if the place feels like you.</h2>', '<h2>Start the conversation</h2>')
c = c.replace('<p>Book a private visit. Walk the estate, see the rooms, understand the food and tell us the story you want to create. No wedding questionnaire before you trust us.</p>', '<p>Tell us your preferred date, approximate guest count and the kind of celebration you have in mind. We will come back with the next steps.</p>')
c = c.replace('<p class="fineprint">This is an enquiry, not a booking. No budget field on the first touch. We read every one and reply by hand.</p>', '')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
