import streamlit as st
import time
from src.ui.base_layout import style_base_layout,style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import create_teacher,check_pass,check_teacher_exists,login_teacher


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type=="register":
        teacher_screen_register()


def teacher_dashboard():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Log Out", type="tertiary",key="loginbackbtn",shortcut='control+backspace'):
            st.session_state.is_logged_in=False
            del st.session_state.teacher_data
            st.rerun()
    st.space()

    teacher_data=st.session_state.teacher_data
    st.header(f"Welcome {teacher_data["name"]}")

    footer_dashboard()

def teacher_login(teacher_username,teacher_pass):
    if not teacher_username or not teacher_pass:
        return False
    teacher=login_teacher(teacher_username,teacher_pass)
    if teacher:
        st.session_state.user_role="teacher"
        st.session_state.teacher_data=teacher
        st.session_state.is_logged_in=True
        return True
    return False

    
def teacher_screen_login():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
         header_dashboard()
    with c2:
         if st.button("Go Back to Home", type="tertiary",key="loginbackbtn",shortcut='control+backspace'):
            st.session_state["login_type"]=None
            st.rerun()
    st.space()
    st.header("Login using password")
    st.space()
    st.space()
    teacher_username=st.text_input("Enter Username",placeholder="Enter username")
    teacher_pass=st.text_input("Enter Password",placeholder="Enter your password",type="password")
    st.divider()

    btnc1,btnc2= st.columns(2)
    with btnc1:
        if st.button("Login", icon=":material/passkey:", width="stretch", shortcut="control+enter",type="secondary"):
            if teacher_login(teacher_username,teacher_pass):
                st.toast("Welcome Back", icon="👋")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password")
    with btnc2:
        if st.button("Register Instead", icon=":material/passkey:", width="stretch", type="secondary"):
            st.session_state.teacher_login_type="register"
            st.rerun()

    footer_dashboard()


def register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass or not teacher_pass_confirm:
        return False, "All feilds are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password dosen't match"

    try:
        create_teacher(teacher_username,teacher_pass,teacher_name)
        return True, "Successfully registred please login!"
    except Exception as e:
        return False, "Unexpected error occured!"


def teacher_screen_register():
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
         header_dashboard()
    with c2:
         if st.button("Go Back to Home", type="tertiary",key="loginbackbtn",shortcut='control+backspace'):
            st.session_state["login_type"]=None
            st.rerun()
    st.space()
    st.header("Register your details")
    
    teacher_username=st.text_input("Enter Username",placeholder="Ex: Omkar@123")
    teacher_name=st.text_input("Enter Your Name",placeholder="Enter your name")
    teacher_pass=st.text_input("Enter Password",placeholder="Enter your password",type="password")
    teacher_pass_confirm=st.text_input("Confirm Password",placeholder="Confirm your password",type="password")
    st.divider()

    btnc1,btnc2= st.columns(2)
    with btnc1:
        if st.button("Register", icon=":material/passkey:", width="stretch", shortcut="control+enter",type="secondary"):
            success,message=register_teacher(teacher_username,teacher_name,teacher_pass,teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(2)
                st.session_state.teacher_login_type="login"
                st.rerun()
            else:
                st.error(message)
    with btnc2:
        if st.button("Login", icon=":material/passkey:", width="stretch", type="secondary"):
            st.session_state.teacher_login_type="login"
            st.rerun()
    footer_dashboard()
    

