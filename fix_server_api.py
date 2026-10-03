import os

f = 'vps-setup/server.js'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    "import verifyRecaptchaHandler from './api/verify-recaptcha.js';",
    "import verifyRecaptchaHandler from './api/verify-recaptcha.js';\nimport enquireHandler from './api/enquire.js';"
)

c = c.replace(
    "app.all('/api/verify-recaptcha', verifyRecaptchaHandler);",
    "app.all('/api/verify-recaptcha', verifyRecaptchaHandler);\napp.all('/api/enquire', enquireHandler);"
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)