import re

f = 'guest.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# 1. Remove scripts
c = re.sub(r'<script src="https://checkout.razorpay.com/v1/checkout.js"></script>\s*', '', c)
c = re.sub(r'<script src="https://www.google.com/recaptcha/api.js".*?></script>\s*', '', c)

# 2. Modify renderGuestBlock to remove gStep2
c = re.sub(
    r"'<div id=\"gStep2\".*?'</div>'\+",
    "",
    c,
    flags=re.DOTALL
)

# 3. Modify send() function
old_send = '''        function send(){
          var name = g('gfName').value.trim(), email = g('gfEmail').value.trim(), phone = d(g('gfPhone').value);
          if(name.length < 2){ g('gfErr1').textContent='Please enter your name.'; g('gfName').focus(); return; }
          if(!validEmail(email)){ g('gfErr1').textContent='Please enter a valid email.'; g('gfEmail').focus(); return; }
          if(phone.length !== 10){ g('gfErr1').textContent='Please enter a valid 10-digit number.'; g('gfPhone').focus(); return; }
          g('gfErr1').textContent='';
          
          cur = { name:name, email:email, phone:phone };
          step(2);
        }'''

new_send = '''        function send(){
          var name = g('gfName').value.trim(), email = g('gfEmail').value.trim(), phone = d(g('gfPhone').value);
          if(name.length < 2){ g('gfErr1').textContent='Please enter your name.'; g('gfName').focus(); return; }
          if(!validEmail(email)){ g('gfErr1').textContent='Please enter a valid email.'; g('gfEmail').focus(); return; }
          if(phone.length !== 10){ g('gfErr1').textContent='Please enter a valid 10-digit number.'; g('gfPhone').focus(); return; }
          g('gfErr1').textContent='';
          
          booking = S.update(booking.id, { guest: { name: name, email: email, phone: pretty(phone), whatsapp: pretty(phone), phoneVerified: true } });
          renderGuestBlock();
          renderCtas();
        }'''
c = c.replace(old_send, new_send)

# 4. Remove verify() function completely
c = re.sub(r'\s*async function verify\(\)\{.*?\n        \}\n', '\n', c, flags=re.DOTALL)

# 5. Remove step(n) logic referencing grecaptcha
old_step = '''        function step(n){ 
          g('gStep1').hidden = n!==1; 
          g('gStep2').hidden = n!==2; 
          if (n === 2 && window.grecaptcha && window.grecaptcha.render) {
              // Re-render explicitly if needed (usually auto-rendered by api.js)
              try { window.grecaptcha.reset(); } catch(e) {}
          }
        }'''
new_step = '''        function step(n){ 
          g('gStep1').hidden = false; 
        }'''
c = c.replace(old_step, new_step)

# 6. Also remove g('gfVerify').addEventListener and g('gfEdit').addEventListener if they exist
c = re.sub(r"g\('gfVerify'\)\.addEventListener.*?;\n", "", c)
c = re.sub(r"g\('gfEdit'\)\.addEventListener.*?;\n", "", c)

# 7. Modify the checkout logic to bypass Razorpay
checkout_regex = r"(\s*)// Calculate total amount including taxes to charge guest.*?var rzp1 = new Razorpay\(options\);\s*rzp1\.open\(\);\s*return;\s*"
replacement = r"\1S.markConfirmed(booking.id);\1location.reload();\1return;\1"

c = re.sub(checkout_regex, replacement, c, flags=re.DOTALL)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
