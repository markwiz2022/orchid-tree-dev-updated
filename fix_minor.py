import os
import glob

# Check-in Check-out in content.js and faq.html
content_js = 'shared/content.js'
with open(content_js, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('Check-in is from 2 PM', 'Check-in: 2 PM onwards')
text = text.replace('check-out is by 11 AM', 'Check-out: by 11 AM')
text = text.replace('a massage can be added whenever you like', '1 full-body massage per room per night + 1 15-minute Kansa foot massage for every guest')

# In content.js: "Full refund if cancelled 48 hours or more before check-in." 
# Make sure old massage texts are replaced.
with open(content_js, 'w', encoding='utf-8') as f:
    f.write(text)

faq = 'faq.html'
with open(faq, 'r', encoding='utf-8') as f:
    faq_text = f.read()
faq_text = faq_text.replace('Check-in is from 2 PM and check-out is by 11 AM.', 'Check-in: 2 PM onwards and Check-out: by 11 AM.')
with open(faq, 'w', encoding='utf-8') as f:
    f.write(faq_text)

# Also fix "massage is an optional add-on" if it exists in content.js
if 'massage is an optional add-on' in text:
    print('Found massage add-on in content.js')

print("Applied checkin and massage fixes.")
