import re

f = 'guest.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

# Normalize line endings for safe matching
c = c.replace('\r\n', '\n')

# 1. Remove script tags
c = c.replace('<script src="https://checkout.razorpay.com/v1/checkout.js"></script>', '')
c = c.replace('<script src="https://www.google.com/recaptcha/api.js" async defer></script>', '')

# 2. Modify gb.innerHTML with regex for whitespace robustness
c = re.sub(
    r"'<div id=\"gStep2\" hidden>'.*?'</div>'\+\s*'</div>';",
    "'</div>';",
    c,
    flags=re.DOTALL
)

# 3. Modify send function
old_send = r'''        function send\(\)\{
          var name = g\('gfName'\)\.value\.trim\(\), email = g\('gfEmail'\)\.value\.trim\(\), phone = d\('gfPhone'\)\.value\);
          if\(name\.length < 2\)\{ g\('gfErr1'\)\.textContent='Please enter your name.'; g\('gfName'\)\.focus\(\); return; \}
          if\(!validEmail\(email\)\)\{ g\('gfErr1'\)\.textContent='Please enter a valid email.'; g\('gfEmail'\)\.focus\(\); return; \}
          if\(phone\.length !== 10\)\{ g\('gfErr1'\)\.textContent='Please enter a valid 10-digit number.'; g\('gfPhone'\)\.focus\(\); return; \}
          g\('gfErr1'\)\.textContent='';
          
          cur = \{ name:name, email:email, phone:phone \};
          step\(2\);
        \}'''

# Wait, d('gfPhone').value) was d(g('gfPhone').value);!
c = re.sub(r'          cur = { name:name, email:email, phone:phone };\s*step\(2\);', r'''          booking = S.update(booking.id, { guest: { name: name, email: email, phone: pretty(phone), whatsapp: pretty(phone), phoneVerified: true } });
          renderGuestBlock();
          renderCtas();''', c)

# 4. Remove wireGuestForm listeners
c = re.sub(r"g\('gfVerify'\)\.addEventListener.*?;\n", "", c)
c = re.sub(r"g\('gfEdit'\)\.addEventListener.*?;\n", "", c)

# 5. Remove verify function explicitly
c = re.sub(r'\s*async function verify\(\)\{.*?btn\.style\.pointerEvents = \'auto\';\n\s*\}\n\s*\}\n', '\n', c, flags=re.DOTALL)

# 6. Replace the razorpay logic inside checkout
c = re.sub(r'\s*// Calculate total amount including taxes to charge guest.*?var rzp1 = new Razorpay\(options\);\s*rzp1\.open\(\);\s*return;', r'''
            // Bypass Payment Gateway
            S.markConfirmed(booking.id);
            location.reload(); 
            return;''', c, flags=re.DOTALL)

# Remove step(n) function which is no longer needed
c = re.sub(r'\s*function step\(n\)\{.*?\}\n', '\n', c, flags=re.DOTALL)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
