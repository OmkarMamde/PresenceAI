import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    subject_code=st.text_input("Enter subject code", placeholder="CS101")
    name=st.text_input("Enter subject name", placeholder="Introduction to CSE")
    section=st.text_input("Enter section", placeholder="A")
    if st.button("Create Subject", type="primary",width="stretch", key=f"create_{name}"):
        if subject_code and name and section:
            create_subject(subject_code,name,section,teacher_id)
            st.toast("Subject created successfully")
            st.rerun()
        else:
            st.info("All feilds are required")
    