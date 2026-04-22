import cv2
import numpy as np

# 🔍 Face Detection
def detect_face(image):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    return faces, img


# ✂️ Extract Face Region
def get_face_region(img, faces):
    for (x, y, w, h) in faces:
        return img[y:y+h, x:x+w]
    return None


# 🎨 Skin Tone Detection (simple logic)
def detect_skin_tone(face):
    avg_color = np.mean(face, axis=(0, 1))

    # Using brightness (approximation)
    if avg_color[0] > 180:
        return "Fair"
    elif avg_color[0] > 120:
        return "Medium"
    else:
        return "Dark"


# 💄 Makeup Recommendation System (FULL VERSION)
def recommend_makeup(skin_tone):

    if skin_tone == "Fair":
        return {
            "Foundation": "Light ivory or porcelain shade with dewy finish ✨",
            "Concealer": "1 shade lighter for bright under-eyes 💫",
            "Blush": "Soft pink or peach tones 🌸",
            "Contour": "Light contour with cool undertones 🌿",
            "Highlighter": "Champagne or pearl glow ✨",
            "Eyeshadow": "Rose gold, champagne, soft brown 💕",
            "Eyeliner": "Brown or soft black liner 👀",
            "Mascara": "Lengthening mascara 💖",
            "Lipstick": "Soft pink, peach nude, gloss 💄"
        }

    elif skin_tone == "Medium":
        return {
            "Foundation": "Warm beige or golden undertone foundation ✨",
            "Concealer": "Brightening concealer with warm tones 💫",
            "Blush": "Coral, peach, warm rose 🍑",
            "Contour": "Warm contour for natural sculpt 🌞",
            "Highlighter": "Golden glow ✨",
            "Eyeshadow": "Bronze, copper, warm brown 🔥",
            "Eyeliner": "Dark brown or black 👁️",
            "Mascara": "Volumizing mascara 💖",
            "Lipstick": "Coral, warm nude, terracotta 💄"
        }

    else:  # Dark
        return {
            "Foundation": "Rich deep tones with warm undertone ✨",
            "Concealer": "Golden or orange corrector + concealer 💫",
            "Blush": "Berry, deep red, plum 🍷",
            "Contour": "Deep contour shades for definition 🌑",
            "Highlighter": "Gold or bronze glow ✨",
            "Eyeshadow": "Gold, purple, deep brown 💜",
            "Eyeliner": "Jet black liner 👁️",
            "Mascara": "Volumizing & curling mascara 💖",
            "Lipstick": "Deep red, plum, bold berry 💄"
        }
