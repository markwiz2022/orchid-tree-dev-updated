import os
import re

files = ['corporate.html', 'weddings.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Replace the JS form handling
    old_js = '''      var form = document.getElementById('enqForm');
      if(form){
        form.addEventListener('submit', function(ev){
          ev.preventDefault();
          var url = 'mailto:orchidtree.blr@gmail.com?subject=' + encodeURIComponent('Wedding event enquiry')
            + '&body=' + encodeURIComponent(buildMessage());
          window.location.href = url;
        });
      }
      var emailLink = document.getElementById('enqEmailBtn');
      if(emailLink){
        emailLink.addEventListener('click', function(){
          var url = 'mailto:orchidtree.blr@gmail.com?subject=' + encodeURIComponent('Wedding private visit enquiry')
            + '&body=' + encodeURIComponent(buildMessage());
          window.location.href = url;
        });
      }'''

    new_js = '''      var form = document.getElementById('enqForm');
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
      
    c = c.replace(old_js, new_js)

    old_js_corp = '''      var form = document.getElementById('enqForm');
      if(form){
        form.addEventListener('submit', function(ev){
          ev.preventDefault();
          var url = 'mailto:orchidtree.blr@gmail.com?subject=' + encodeURIComponent('Corporate event enquiry')
            + '&body=' + encodeURIComponent(buildMessage());
          window.location.href = url;
        });
      }
      var emailLink = document.getElementById('enqEmailBtn');
      if(emailLink){
        emailLink.addEventListener('click', function(){
          var url = 'mailto:orchidtree.blr@gmail.com?subject=' + encodeURIComponent('Corporate event enquiry')
            + '&body=' + encodeURIComponent(buildMessage());
          window.location.href = url;
        });
      }'''
    
    c = c.replace(old_js_corp, new_js)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
