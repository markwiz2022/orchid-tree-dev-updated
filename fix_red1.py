import os

files_to_fix = ['home.html', 'faq.html']
for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Home and FAQ exact match
    old_str1 = "Yes. The estate hosts intimate weddings, celebrations, and corporate offsites, with a full buyout of all eleven rooms."
    new_str1 = "Yes. The estate hosts intimate weddings, celebrations and corporate offsites. Corporate programmes can be arranged as specific event-space reservations or as an exclusive full-estate buyout, depending on the programme."
    content = content.replace(old_str1, new_str1)
    
    # FAQ slight variation
    old_str1b = "Yes. The estate hosts intimate weddings, celebrations and corporate offsites, with a full buyout of all eleven rooms."
    content = content.replace(old_str1b, new_str1)

    old_str2 = "Yes. The whole estate - all eleven rooms - can be bought out for weddings, family gatherings or company offsites. Message the team to plan it."
    new_str2 = "Yes. Weddings and private gatherings can be arranged as full-estate buyouts. Corporate programmes can be arranged as specific event-space reservations or as exclusive full-estate buyouts, depending on the programme."
    content = content.replace(old_str2, new_str2)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
