import streamlit as st
import base64
from pathlib import Path

def get_base64(path):
    with open(path,"rb") as f:
        return base64.b64encode(f.read()).decode()
BASE_DIR = Path(__file__).resolve().parents[2]
mascot = get_base64(BASE_DIR / "images" / "mascot.png")

def header_home():
    st.markdown(f"""
                <div style='align-items:center; justify-content:center; display:flex; flex-direction:column; '>
            
                <img src='data:image/png;base64,{mascot}' style='height:130px;'>
                <h1 style='text-align:center; line-height:0; '>Presence<br/>AI </h1>
            
                </div>
                """,unsafe_allow_html=True)

def header_dashboard():
    st.markdown(f"""
                <div style='display:flex; align-items:center; justify-content:center; gap:10px;'>
                <img src='data:image/png;base64,{mascot}' style='height:85px;'> 
                <h2 style='text-align:left;'>Presence<br/>AI</h2>
                </div>

                """,unsafe_allow_html=True)