import os

file_path = 'shared/nav.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Vercel redirect we added earlier
redirect_code = '''
  // Force redirect from Vercel to official domain
  if (window.location.hostname.indexOf('vercel.app') !== -1) {
    window.location.href = window.location.href.replace(window.location.hostname, 'orchidtree.in');
  }
'''

if redirect_code in content:
    content = content.replace(redirect_code, "")
    print("Successfully removed Vercel redirect.")
else:
    print("Could not find the exact Vercel redirect string.")

# Add Mouseflow tracking script, but ensure it DOES NOT run on Vercel
mouseflow_code = '''
  // Mouseflow Tracking (Disabled on Vercel preview)
  if (window.location.hostname.indexOf('vercel.app') === -1) {
    window._mfq = window._mfq || [];
    (function() {
      var mf = document.createElement("script");
      mf.type = "text/javascript"; mf.defer = true;
      mf.src = "//cdn.mouseflow.com/projects/3bd0c727-dcd7-4e63-b077-603170ced523.js";
      document.getElementsByTagName("head")[0].appendChild(mf);
    })();
  }
'''

# Add it just before the closing of the IIFE if possible, or just append it inside.
content = content.replace("})();", mouseflow_code + "\n})();")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
