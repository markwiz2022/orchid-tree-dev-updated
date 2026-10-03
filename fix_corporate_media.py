import os
import glob

f = 'corporate.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace('<div class="media" style="flex:0 0 50%;min-height:520px;">', '<div class="media">')

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
