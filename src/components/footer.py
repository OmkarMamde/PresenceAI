import streamlit as st
import base64
from pathlib import Path

def get_base64(path):
    with open(path,"rb") as f:
        return base64.b64encode(f.read()).decode()
BASE_DIR = Path(__file__).resolve().parents[2]
mascot = get_base64(BASE_DIR / "images" / "logo.png")

def footer_home():
    st.markdown(f"""
                <div style='display:flex;  justify-content:center; items-align:center; margin-top:2rem; gap:6px'>
                <p style='font-weight:bold; color:black; '>Created with ❤️ by</p>
                <img src='data:image/png;base64,{img}' style='max-height:27px;'>
                </div>

                """,unsafe_allow_html=True)
    
def footer_dashboard():
    st.markdown(f"""
               <div style='display:flex;  justify-content:center; items-align:center; margin-top:1rem; gap:6px'>
                <p style='font-weight:bold; color:black; '>Created with ❤️ by</p>
                <img src='data:image/png;base64,{img}' style='max-height:27px;'>
                </div>

                """,unsafe_allow_html=True)