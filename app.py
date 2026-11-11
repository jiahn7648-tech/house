import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="나의 픽셀 하우스", page_icon="🏠", layout="wide")

ROOT = Path(__file__).parent
html = (ROOT / "game" / "index.html").read_text(encoding="utf-8")

st.markdown(
    """
    <style>
      .block-container {max-width: 1200px; padding-top: 1.2rem;}
      header, footer {visibility: hidden;}
      .stApp {background: #171717;}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("🏠 나의 픽셀 하우스")
st.caption("WASD 또는 방향키로 이동 · 물건을 클릭하거나 가까이에서 E 키를 눌러 상호작용")
components.html(html, height=760, scrolling=False)
