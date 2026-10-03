import os

f = 'blog-farm-to-table-dining-near-bangalore.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# The current HTML has:
# <a class="primary" href="blog-farm-to-table-dining-near-bangalore.html">Read about dining at Orchid Tree</a>
c = c.replace(
    '<a class="primary" href="blog-farm-to-table-dining-near-bangalore.html">Read about dining at Orchid Tree</a>',
    '<a class="primary" href="plan-your-dining.html">Plan your dining before arrival &rarr;</a>'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
