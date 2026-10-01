import os

f = 'faq.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

old_faq = 'Across all eleven rooms the estate comfortably hosts a large group - ideal for full-property buyouts.'
new_faq = 'Across all eleven rooms the estate comfortably hosts up to 34 adults - ideal for full-property buyouts.'
c = c.replace(old_faq, new_faq)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
