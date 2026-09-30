import os

files_to_fix = ['index.html', 'orchidtree-home-wireframe.html']
for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_str1 = "Yes. The estate hosts intimate weddings, celebrations, and corporate offsites, with a full buyout of all eleven rooms."
    new_str1 = "Yes. The estate hosts intimate weddings, celebrations and corporate offsites. Corporate programmes can be arranged as specific event-space reservations or as an exclusive full-estate buyout, depending on the programme."
    content = content.replace(old_str1, new_str1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
