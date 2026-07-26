import streamlit as st
def teacher_screen():
    st.header('teacher screen')

    if st.button("Home"):
        st.session_state["login_type"]=None
        st.rerun()