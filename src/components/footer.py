import streamlit as st
import base64

def get_base64(path):
    with open(path,"rb") as f:
        return base64.b64encode(f.read()).decode()
img=get_base64(".\\images\\logo.png")

def footer_home():
    st.markdown(f"""
                <div style='display:flex;  justify-content:center; items-align:center; margin-top:2rem; gap:6px'>
                <p style='font-weight:bold; color:black; '>Created with ❤️ by</p>
                <img src='data:image/png;base64,{img}' style='max-height:27px;'>
                </div>

                """,unsafe_allow_html=True)