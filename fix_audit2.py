import os
import glob

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Replaced in {filepath}")

# BLUE 2
replace_in_file('corporate.html', 'While you plan it, see the <a href="experiences.html">experiences on the estate</a>, the, or read more <a href="about.html">about Orchid Tree</a>.', 'While you plan, explore the <a href="experiences.html">experiences on the estate</a> or read more <a href="about.html">about Orchid Tree</a>.')

# ORANGE 6
replace_in_file('corporate.html', 'For corporate programs, the proposal clearly states the spaces or full-estate exclusivity being reserved for your dates.', 'Depending on the programme, bookings may reserve specific event spaces or the full estate. Your proposal will state the exact exclusivity included.')

# ORANGE 5
replace_in_file('corporate.html', 'Viva Farm can be added by arrangement for larger residential groups, up to around 60.', 'Up to approximately 60 overnight guests with Viva Farm, by arrangement.')

# BLUE 4 (Check if "the restaurant" needs replacing in FAQ/Stays)
# Checked previously, most were replaced. 

