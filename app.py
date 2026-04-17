import streamlit as st
from PIL import Image
import google.generativeai as genai

st.set_page_config(page_title="LAWADE KI SHAKTI", page_icon="🧠", layout="wide")

# Dark Theme
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .header { font-size: 38px; font-weight: bold; color: #00FFAA; letter-spacing: 2px; text-align: center; }
    .warning { font-size: 22px; color: #FF5555; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Password Protection
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown('<p class="header">LAWADE KI SHAKTI</p>', unsafe_allow_html=True)
    st.markdown('<p class="warning">KHOLNA MAT</p>', unsafe_allow_html=True)
    
    password = st.text_input("Password Daalo", type="password")
    
    if st.button("Enter", type="primary"):
        if password == "PRIYANKA PRATAP":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Kon hai tu Madharchod")
    st.stop()

# =============== MAIN APP ===============

st.markdown('<p class="header">LAWADE KI SHAKTI</p>', unsafe_allow_html=True)
st.markdown("**KHOOFIYA GUFAA**")

st.caption("Gaand fate to rona mat")

st.markdown("---")

api_key = st.text_input("🔑 Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

# Funny Emoji ke saath simple line
st.markdown("### Gaand dikha")
uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True, caption="Uploaded Chart")

    if st.button("▶ ANALYZE CHART", type="primary", use_container_width=True):
        if not api_key:
            st.error("Pehle Gemini API Key daalo")
        else:
            with st.spinner("LAWADE KI SHAKTI soch raha hai..."):
                try:
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    prompt = """
You are a highly experienced Nifty 50 trader. Analyze the chart carefully with VWAP and Volume Profile.

Give output in clean format:

**Market Structure:** Bullish / Bearish / Choppy
**Key Observations:**
**Trade Setup:**
- Direction: Long / Short / Wait
- Entry Zone:
- Stop Loss:
- Target 1:
- Target 2:
- Risk:Reward: 1:X
**Confidence:** High / Medium / Low
**Reasoning:**
"""

                    response = model.generate_content([prompt, image])
                    st.success("✅ LAWADE KI SHAKTI ne Analysis Kar Diya!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

st.caption("Gaand fate to rona mat")