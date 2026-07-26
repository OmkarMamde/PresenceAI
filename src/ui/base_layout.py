import streamlit as st

def style_background_home():
    st.markdown("""
                <style>
                .stApp{
                background:linear-gradient(
                135deg,
                #ffffff 0%,
                #eef6ff 30%,
                #dbeafe 65%,
                #c7d2fe 100%
                ) !important;
                color:black !important;
                
                }
                div[data-testid="stMainBlockContainer"] {
                padding:2rem 1rem 10rem !important;
                }
                .stApp div[data-testid="stColumn"]{
                background:#ffffff !important;
                border:2px solid #e5e7eb !important;
                box-shadow:0 12px 30px rgba(0,0,0,0.08) !important;
                padding:1rem !important;
                border-radius:30px !important;
                
                }
               
                

                
                </style>

                """,unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@100..900&display=swap');
                
                #MainMenu,header,footer{
                visibility:hidden !important;
                }
                .block-container{
                padding-top:1.5rem !important;
                }
                
                h1{
                font-family:"Sora", sans-serif !important;
                font-size:3rem !important;
                font-weight:800 !important;
                line-height:1!important;
                margin-top:0rem !important;
                margin-bottom:0rem !important;
                padding-top:0rem !important;
                }
                h2{
                font-family:"Sora", sans-serif !important;
                font-size:2rem !important;
                font-weight:600 !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                }
                h3,h4,p{
                font-family:"Inter", sans-serif !important; 
                }
                button[kind="primary"]{
                border-radius:1.5rem !important;
                background:#4f46e5 !important;
                color:white;
                padding:10px 20px !important;
                border:None !important;
                transition:transform 0.25s ease-in-out !important;
                }
                button[kind="secondary"]{
                border-radius:1.5rem !important;
                background:#111827 !important;
                color:white !important;
                padding:10px 20px !important;
                border:None !important;
                transition:transform 0.25s ease-in-out !important;
                }
                button[kind="tertiary"]{
                border-radius:1.5rem !important;
                background:#ff4d8d !important;
                color:white !important;
                padding:10px 20px !important;
                border:None !important;
                transition:transform 0.25s ease-in-out !important;
                }
                button[kind="primary"]:hover{
                transform:scale(1.05) !important;
                background:#4338CA !important;
                }
                button[kind="secondary"]:hover{
                transform:scale(1.05) !important;
                background:#1f2937 !important;
                }
                button[kind="tertiary"]:hover{
                transform:scale(1.05) !important;
                background:#ed1862 !important;
                }

                </style>

                """,unsafe_allow_html=True)