import os
import re

f = 'weddings.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('<h2>Intimate does not mean tiny.</h2>', '<h2>The numbers, at a glance</h2>')
c = c.replace('<p class="muted" style="margin-top:16px;max-width:720px;"></p>', '<p class="muted" style="margin-top:16px;max-width:720px;">Up to 200 celebration guests, with accommodation for approximately 60 resident guests across Orchid Tree and associated Viva Farm accommodation.</p>')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)

