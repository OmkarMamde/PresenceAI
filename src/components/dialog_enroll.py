import streamlit as st
from src.database.config import supabase
import time
from src.database.db import enroll_student_to_subject

@st.dialog("Enroll in subject")
def enroll_dialog():
    student_id=st.session_state.student_data["student_id"]
    st.write("Enter subject code provided by your teacher to enroll")
    subject_code=st.text_input("Enter subject code")
    if st.button("Enroll", width="stretch"):
        if subject_code:
            response=supabase.table("subjects").select("*").eq("subject_code",subject_code).execute()
            if response.data:
                subject=response.data[0]
                check=supabase.table("subject_students").select("*").eq("student_id",student_id).eq("subject_id",subject["subject_id"]).execute()
                if check.data:
                    st.warning("You are already enrolled")
                else:
                    enroll_student_to_subject(student_id,subject["subject_id"])
                    st.success(f"Enrolled successfully in {subject['name']}")
                    time.sleep(1)
                    st.rerun()
            
        else:
            st.warning("Enter subject code")
