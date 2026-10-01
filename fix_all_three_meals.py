import glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    
    # Simple replacements
    c = c.replace('all three meals-breakfast, lunch and dinner-are included', 'breakfast, lunch, dinner, high tea and snacks are included')
    c = c.replace('All three meals are plated', 'Meals are plated')
    c = c.replace('all three meals, high tea and snacks', 'breakfast, lunch, dinner, high tea and snacks')
    c = c.replace('all three meals, high tea, snacks', 'breakfast, lunch, dinner, high tea and snacks')
    c = c.replace('All three meals are included with every stay - breakfast, lunch and dinner.', 'Overnight stays include breakfast, lunch, dinner, high tea and snacks.')
    c = c.replace('all three meals, wellness', 'breakfast, lunch, dinner, high tea and snacks, wellness')
    c = c.replace('all three meals', 'breakfast, lunch, dinner, high tea and snacks')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)
