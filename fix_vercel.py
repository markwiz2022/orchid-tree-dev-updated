import os
import json

f = 'vercel.json'
with open(f, 'r', encoding='utf-8') as file:
    data = json.load(file)

data['redirects'].extend([
    {
      "source": "/restaurant.html",
      "destination": "/blog-farm-to-table-dining-near-bangalore.html",
      "permanent": True
    },
    {
      "source": "/restaurant",
      "destination": "/blog-farm-to-table-dining-near-bangalore.html",
      "permanent": True
    }
])

with open(f, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2)
