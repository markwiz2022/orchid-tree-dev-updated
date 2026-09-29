import os

file_path = 'book-packages.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        "      return '<div class=\"price-block\">'+\n        '<div class=\"all-in\"><span class=\"amt\">'+rupees(subtotal)+'</span>'+\n          '<span class=\"lbl\">all-in for '+plural(nights, 'night', 'nights')+'</span></div>'+\n        '<div class=\"tax\">+18% tax at checkout</div>'+ perLine +\n      '</div>';",
        "      return '<div class=\"price-block\">'+\n        '<div class=\"all-in\"><span class=\"amt\">'+rupees(subtotal)+'</span>'+\n          '<span class=\"lbl\">all-in for '+plural(nights, 'night', 'nights')+'</span></div>'+\n        '<div class=\"tax\">+18% tax at checkout</div>'+ perLine +\n        '<div style=\"font-size:12px;color:var(--gold);margin-top:10px;font-weight:600;\">3 meals + wellness + full estate access included</div>'+\n      '</div>';"
    )
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:30]}...")
    else:
        print(f"NOT FOUND: {old[:30]}...")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
