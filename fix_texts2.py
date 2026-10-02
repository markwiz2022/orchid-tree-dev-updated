import os

f1 = 'blog-intimate-wedding-venues-near-bangalore.html'
with open(f1, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    '''and applicable government charges are extra.</p></div></div>''',
    '''and applicable government charges are extra. Please discuss the arrangements with our event team during planning.</p></div></div>'''
)

with open(f1, 'w', encoding='utf-8') as file:
    file.write(c)