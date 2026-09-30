import os

exact_old = "Children aged 0-8 can be selected during booking. Children aged 7-8 may require additional charges."
exact_new = "Children aged 0–8 can be included in the booking. Children aged 0–6 may use existing bedding; additional bedding for older children is subject to availability and applicable charges."

for filepath in ['home.html', 'index.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if exact_old in content:
        content = content.replace(exact_old, exact_new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Success replacing in {filepath}")
    else:
        print(f"Not found in {filepath}")

