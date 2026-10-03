import os
import re

f = 'host-with-us.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

script_to_add = '''
      function v(id){ var el = document.getElementById(id); return el ? el.value.trim() : ''; }
      function buildMessage(){
        var lines = [
          'Hi Orchid Tree, we would love to enquire about a gathering.',
          v('enqName')   ? 'Name: ' + v('enqName') : '',
          v('enqEmailIn')? 'Email: ' + v('enqEmailIn') : '',
          v('enqType')   ? 'Gathering type: ' + v('enqType') : '',
          v('enqDate')   ? 'Preferred date: ' + v('enqDate') : '',
          v('enqGuests') ? 'Guests: ' + v('enqGuests') : ''
        ];
        return lines.filter(Boolean).join('\\n');
      }
      var form = document.getElementById('enqForm');
      if(form){
        form.addEventListener('submit', function(ev){
          ev.preventDefault();
          var btn = form.querySelector('button[type="submit"]');
          var originalText = btn.innerHTML;
          btn.innerHTML = 'Submitting...';
          btn.disabled = true;
          
          fetch('/api/enquire', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message: buildMessage() })
          }).then(function() {
            btn.innerHTML = 'Enquiry submitted';
            setTimeout(function(){ btn.innerHTML = originalText; btn.disabled = false; form.reset(); }, 4000);
          }).catch(function() {
            btn.innerHTML = 'Error. Try again';
            setTimeout(function(){ btn.innerHTML = originalText; btn.disabled = false; }, 3000);
          });
        });
      }

'''

c = c.replace("// ---- nav solidify on scroll ----", script_to_add + "      // ---- nav solidify on scroll ----")

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
