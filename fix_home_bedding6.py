import os
import re

exact_new = "Children aged 0–8 can be selected during booking. Children aged 7–8 may incur an additional charge depending on the room and bedding arrangement. Any applicable charge will be shown before booking confirmation."

for filepath in ['home.html', 'index.html', 'orchidtree-home-wireframe.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace the content inside <div class="rc-note">...</div> that starts with "Children aged 0"
    content = re.sub(r'<div class="rc-note">Children aged 0.*?</div>', f'<div class="rc-note">{exact_new}</div>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
