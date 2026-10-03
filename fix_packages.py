import os

f = 'shared/packages.js'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()

c = c.replace(
    'function generateSingleRooms(group) {',
    'function generateSingleRooms(group) {\n    if (groupTotal(group) > 34) return [];'
)

c = c.replace(
    'function generatePackages(group) {',
    'function generatePackages(group) {\n    if (groupTotal(group) > 34) return [];'
)

with open(f, 'w', encoding='utf-8') as file:
    file.write(c)