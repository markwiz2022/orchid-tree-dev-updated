import os

file_path = 'shared/nav.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

redirect_code = '''
  // Force redirect from Vercel to official domain
  if (window.location.hostname.indexOf('vercel.app') !== -1) {
    window.location.href = window.location.href.replace(window.location.hostname, 'orchidtree.in');
  }
'''

content = content.replace("(function () {", "(function () {\n" + redirect_code)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
