import os
import re

for f in ['home.html', 'index.html', 'orchidtree-home-wireframe.html']:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    old_dates = '''            <div class="rc-dates">
              <label class="rc-date"><span class="k">Arrive</span><input type="date" id="rcArrive" aria-label="Arrive"></label>
              <label class="rc-date"><span class="k">Leave</span><input type="date" id="rcLeave" aria-label="Leave"></label>
            </div>'''
    
    new_dates = '''            <div class="rc-dates">
              <label class="rc-date"><span class="k">Arrive</span><input type="date" id="rcArrive" aria-label="Arrive"></label>
              <label class="rc-date"><span class="k">Leave</span><input type="date" id="rcLeave" aria-label="Leave"></label>
            </div>
            <div class="rc-note" style="margin-top:4px; margin-bottom:12px; text-align:center;">Check-in from 2 PM &middot; Check-out by 11 AM</div>'''
            
    c = c.replace(old_dates, new_dates)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

