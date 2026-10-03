import os
import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Fix specificity for foot-social links
    c = c.replace('.foot-social a{width:38px', 'footer .foot-social a{width:38px')
    c = c.replace('.foot-social a svg{width:17px', 'footer .foot-social a svg{width:17px')
    c = c.replace('.foot-social a:hover{background:', 'footer .foot-social a:hover{background:')
    
    # While we're here, let's fix .hero-inner in all pages just in case they have the same overlap issue
    c = c.replace(
        '.hero-inner{position:relative;z-index:2;padding:0 var(--pad) clamp(40px,7vh,80px);width:100%;}',
        '.hero-inner{position:relative;z-index:2;padding:120px var(--pad) clamp(40px,7vh,80px);width:100%;}'
    )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
