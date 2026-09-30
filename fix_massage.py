import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # We want to replace "one full-body massage per room" (and capitalized) that is NOT followed by " per night"
    # Negative lookahead: (?!\s*per night)
    new_c = re.sub(r'(?i)(one full-body massage per room)(?!\s*per night)', r'\1 per night', c)
    
    if new_c != c:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_c)
        print(f"Replaced massage in {f}")

