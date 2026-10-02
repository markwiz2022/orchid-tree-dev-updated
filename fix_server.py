import os

f = 'vps-setup/server.js'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('''app.get('/home(.html)?', (req, res) => {
  res.redirect(301, '/');
});''', '''app.get('/home(.html)?', (req, res) => {
  res.redirect(301, '/');
});

app.get('/restaurant(.html)?', (req, res) => {
  res.redirect(301, '/blog-farm-to-table-dining-near-bangalore.html');
});''')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)