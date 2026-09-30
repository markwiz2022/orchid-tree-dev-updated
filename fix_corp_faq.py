import os

files = ['corporate.html', 'host-with-us.html', 'faq.html']
for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    old_str = "Yes. Orchid Tree has 11 rooms, and Up to approximately 60 overnight guests with Viva Farm, by arrangement."
    new_str = "Yes. Orchid Tree accommodates up to 34 overnight guests across its 11 rooms. Additional accommodation can bring the combined Orchid Tree + Viva Farm capacity to approximately 60 guests, by arrangement."
    
    if old_str in c:
        c = c.replace(old_str, new_str)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(c)
        print(f"Replaced in {f}")
