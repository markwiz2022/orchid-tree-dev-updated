import os
import re

def fix_file(f):
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()

    # Meta and json-ld fixes
    c = c.replace('stay for up to 60', 'stay for up to 34 adults')
    c = c.replace('accommodation for up to 60', 'accommodation for up to 34 adults')
    c = c.replace('stay for up to approximately 60', 'stay for up to 34 adults')
    
    # Specific weddings.html replacements
    c = c.replace(
        '<span class="statnum">60</span> stay</div><div class="l">resident guests</div>',
        '<span class="statnum">34</span> stay</div><div class="l">overnight adults</div>'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

fix_file('corporate.html')
fix_file('weddings.html')
