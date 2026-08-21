import streamlit as st
from src.database.config import supabase
from src.pipelines.voice_pipeline import process_bulk_audio
from datetime import datetime
from src.components.dialog_attendance_result import attendance_result_dialog
import pandas as pd
from src.components.dialog_attendance_result import attendance_result_dialog,show_attendance_results

@st.dialog("Voice Attendance!")
def voice_attendance_dialog(selcted_subject_id):
    st.write("Record a audio saying something like I'm present...")

    audio_data=None
    audio_data=st.audio_input("Record a audio")

    if st.button("Analyze Audio", width="stretch", icon=":material/analytics:"):
        with st.spinner("Analyzing audio data..."):

            enrolled_res=supabase.table("subject_students").select("*,students(*)").eq("subject_id",selcted_subject_id).execute()
            enrolled_students=enrolled_res.data

            if not enrolled_students:
                st.warning("No student enrolled for this subject")
                return

            candidate_dict={
                s["students"]["student_id"]:s["students"]["voice_embeddings"] for s in enrolled_students if s["students"].get("voice_embeddings")
            }

            if not candidate_dict:
                st.error("No enrolled students have voice registered")
                return

            audio_byte=audio_data.read()

            detected_scores=process_bulk_audio(audio_byte,candidate_dict)

            results,attendance_to_logs=[],[]

            current_timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student=node["students"]
                score=detected_scores.get(student["student_id"],0.0)
                is_present=bool(score>0)

                results.append({
                    "Name":student["name"],
                    "ID":student["student_id"],
                    "Source":score if is_present else "-",
                    "status":"✅ present" if is_present else "❌ absent"
                })

                attendance_to_logs.append({
                    "student_id":student["student_id"],
                    "subject_id":selcted_subject_id,
                    "timestamp":current_timestamp,
                    "is_present":bool(is_present)
                })
            st.session_state.voice_attendance_results=(pd.DataFrame(results),attendance_to_logs)

    if st.session_state.get("voice_attendance_results"):
        st.divider()
        df_results,attendance_to_logs=st.session_state.voice_attendance_results
        show_attendance_results(df_results,attendance_to_logs)