import os

filepath = 'faq.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix FAQ meal contradictions
content = content.replace("the restaurant covers breakfast, and lunch and dinner can be pre-booked and cooked fresh to your taste.", "all three meals are included and cooked fresh for you by our kitchen.")
content = content.replace("Can I pre-order lunch and dinner?", "Can I share my meal preferences?")
content = content.replace("Yes, and we recommend it. Lunch and dinner are pre-booked so your meals are ready, fresh, when you arrive.", "Yes. Meals are planned around your preferences, so we recommend sharing dietary needs and choices before you arrive.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated faq.html")
