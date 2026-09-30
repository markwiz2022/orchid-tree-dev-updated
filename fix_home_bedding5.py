import os
import re

for filepath in ['home.html', 'index.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'<div class="rc-note">.*?</div>', r'<div class="rc-note">Children aged 0–8 can be included in the booking. Children aged 0–6 may use existing bedding; additional bedding for older children is subject to availability and applicable charges.</div>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
