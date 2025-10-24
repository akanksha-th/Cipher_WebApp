import streamlit as st
import base64
from app import set_background

st.set_page_config(page_title="Violet Cipher", layout="centered")

with open("fonts/VioletScript-Regular.otf", "rb") as f:
    font_data = f.read()
font_base64 = base64.b64encode(font_data).decode()

set_background("assets/violet-evergarden-violets-letter-to-major-gilbert.jpg")

st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'VioletScript';
        src: url(data:font/otf;base64,{font_base64}) format('opentype');
    }}

    textarea, input, .violet {{
        font-family: 'VioletScript' !important;
        font-size: 32px !important;
        color: #3b2a54 !important;
        letter-spacing: 2px;
    }}
    .translation {{
        font-family: monospace;
        font-size: 22px;
        color: #111;
        padding-top: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Violet Cipher")

st.markdown("<h1>🕊️ Violet Script Decoder</h1>", unsafe_allow_html=True)
st.markdown("<p>Type in Violet script (it will look like Violet’s alphabet), and see the English translation appear below.</p>", unsafe_allow_html=True)

# --- Typing Area (shows Violet glyphs) ---
typed_violet = st.text_area("Type in Violet alphabet:", height=150, key="violet_input")

# --- Simple mock translation mapping (A→A, B→B for now) ---
def violet_to_english(text):
    mapping = {chr(i): chr(i) for i in range(65, 91)}  # A-Z identity for demo
    mapping.update({chr(i+32): chr(i) for i in range(65, 91)})  # a-z
    # You can extend this mapping to match your custom alphabet logic
    translated = ''.join(mapping.get(ch, ch) for ch in text)
    return translated

# --- Output (decoded to English) ---
if typed_violet:
    english_text = violet_to_english(typed_violet)
    st.markdown("<h3>🔍 Decoded English:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='translation'>{english_text}</div>", unsafe_allow_html=True)