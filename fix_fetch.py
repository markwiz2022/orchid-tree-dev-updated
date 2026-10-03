import os
import glob

html_files = ['corporate.html', 'weddings.html', 'host-with-us.html']

for f in html_files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
        
        # Replace the fetch call to properly check response.ok
        old_fetch = '''fetch('/api/enquire', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message: buildMessage() })
          }).then(function() {
            btn.innerHTML = 'Enquiry submitted';
            setTimeout(function(){ btn.innerHTML = originalText; btn.disabled = false; form.reset(); }, 4000);
          }).catch(function() {
            btn.innerHTML = 'Error. Try again';
            setTimeout(function(){ btn.innerHTML = originalText; btn.disabled = false; }, 3000);
          });'''
          
        new_fetch = '''fetch('/api/enquire', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message: buildMessage() })
          }).then(function(res) {
            if (!res.ok) throw new Error('Server error');
            return res.json();
          }).then(function() {
            btn.innerHTML = 'Enquiry submitted';
            setTimeout(function(){ btn.innerHTML = originalText; btn.disabled = false; form.reset(); }, 4000);
          }).catch(function() {
            btn.innerHTML = 'Setup required';
            setTimeout(function(){ btn.innerHTML = originalText; btn.disabled = false; }, 4000);
          });'''
          
        c = c.replace(old_fetch, new_fetch)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(c)
