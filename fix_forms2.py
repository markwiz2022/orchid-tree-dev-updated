import os
import re

files = ['corporate.html', 'weddings.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    new_js = '''var form = document.getElementById('enqForm');
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
      }'''
      
    c = re.sub(r"var form = document\.getElementById\('enqForm'\);[\s\S]*?\}\);\s*\}", new_js, c)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)