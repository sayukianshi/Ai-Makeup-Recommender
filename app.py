import streamlit as st
from PIL import Image
import cv2
import numpy as np
import time
from utils import detect_face, get_face_region, detect_skin_tone, recommend_makeup

# Page config
st.set_page_config(page_title="AI Makeup Bestie", layout="centered")

# 🎨 Custom CSS + Fonts
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;500&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #fce7f3, #e0f2fe);
}

/* Title */
.title {
    font-family: 'Pacifico', cursive;
    text-align: center;
    color: #ff6f91;
    font-size: 45px;
    margin-bottom: 10px;
}

/* Upload box */
.upload-box {
    background: #fff0f6;
    border: 2px dashed #ffb6c1;
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 10px;
}

/* Result cards */
.result-box {
    background: #ffffff;
    padding: 15px;
    border-radius: 20px;
    margin: 10px 0;
    box-shadow: 0px 4px 12px rgba(255, 182, 193, 0.4);
}

/* Cute animation */
.bounce {
    animation: bounce 1s infinite;
    font-size: 60px;
    text-align: center;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0);}
    50% { transform: translateY(-15px);}
}
</style>
""", unsafe_allow_html=True)

# 🎀 Title
st.markdown('<div class="title">💖 AI Makeup Bestie 🎀</div>', unsafe_allow_html=True)
st.write("✨ Your Personal Makeup & Skin Guide ✨")

# 📸 Upload UI
st.markdown('<div class="upload-box">📸 Upload your cute selfie 💕</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

# 🚀 Main Logic
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # 🧸 Animation
    st.markdown('<div class="bounce">🧸</div>', unsafe_allow_html=True)
    st.write("Analyzing your beauty... 💕")
    time.sleep(2)

    # Face detection
    faces, img = detect_face(image)

    if len(faces) == 0:
        st.error("No face detected. Try another image.")
    else:
        # Draw rectangle
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        st.image(img, caption="✨ Face Detected", use_column_width=True)

        # Get face
        face = get_face_region(img, faces)

        if face is not None:
            tone = detect_skin_tone(face)
            suggestions = recommend_makeup(tone)

            # 🌸 Results
            st.markdown("## 🌸 Your Glow-Up Results ✨")

            st.markdown(f"""
            <div class="result-box">
            💫 <b>Skin Tone:</b> {tone}
            </div>
            """, unsafe_allow_html=True)

            # 💄 Makeup suggestions
            st.markdown("## 💄 Your Personalized Makeup 💕")

            for key, value in suggestions.items():
                st.markdown(f"""
                <div class="result-box">
                💖 <b>{key}:</b> {value}
                </div>
                """, unsafe_allow_html=True)

            # 💗 Footer
            st.markdown("""
            ---
            💗 Made with love using AI • Your Makeup Bestie 💄✨
            """)
