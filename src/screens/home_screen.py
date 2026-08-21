import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home
from pathlib import Path
# import base64

# def get_base64(path):
#     with open(path,"rb") as f:
#         return base64.b64encode(f.read()).decode()
# teacher_img=get_base64('.\\images\\teacher.png')
# student_img=get_base64(".\images\student.png")

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()
    
    BASE_DIR = Path(__file__).resolve().parents[2]
    col1, col2=st.columns(2,gap="large")

    with col1:
        st.header("I'm Student")
        st.image(BASE_DIR / "images" / "mascot-student.png", width=120)
        # st.image("https://i.ibb.co/844D9Lrt/mascot-teacher.png",width=120)
        if st.button("Student Portal", type="primary", icon=':material/arrow_outward:',icon_position="right"):
            st.session_state["login_type"]="student"
            st.rerun()
            
    with col2:
        st.header("I'm Teacher")
        st.image(BASE_DIR / "images" / "mascot-prof.png",width=150)
        # st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png",width=145)
        if st.button("Teacher Portal",type="tertiary", icon=':material/arrow_outward:', icon_position='right'):
            st.session_state["login_type"]="teacher"
            st.rerun()

    footer_home()
    