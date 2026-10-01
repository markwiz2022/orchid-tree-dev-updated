import os

f = 'vps-setup/server.js'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('app.use(express.static(__dirname));', '''app.get('/home(.html)?', (req, res) => {
  res.redirect(301, '/');
});

app.use(express.static(__dirname));''')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
