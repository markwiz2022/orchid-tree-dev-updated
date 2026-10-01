import pytesseract
from PIL import Image

try:
    img = Image.open('C:/Users/ASUS/.gemini/antigravity/brain/343742f9-0e41-4e4e-abcb-aa0778a3cbb7/.user_uploaded/media_1790868324554.png')
    text = pytesseract.image_to_string(img)
    print("OCR TEXT:")
    print(text)
except Exception as e:
    print("Error:", e)
