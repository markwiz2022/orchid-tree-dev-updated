import os

filepath = 'shared/nav.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

redirect_snippet = '''
  // Redirect old room URLs
  if (window.location.pathname.indexOf('/stays/') !== -1) {
    window.location.href = '/stays.html';
  }
'''

if 'Redirect old room URLs' not in text:
    text = text.replace('})();', redirect_snippet + '\n})();')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

