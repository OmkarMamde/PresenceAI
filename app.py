import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.set_page_config(
        page_title="PresenceAI-Making Attendance Faster Using AI",
        page_icon="./images/mascot.png"
    )

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    join_code = st.query_params.get("join-code")

    # Join link forces student portal
    if join_code and st.session_state["login_type"] != "student":
        st.session_state["login_type"] = "student"
        st.rerun()

    # Display appropriate screen
    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

    # Auto-enroll logged-in student
    if (
        join_code
        and st.session_state.get("is_logged_in")
        and st.session_state.get("user_role") == "student"
    ):
        auto_enroll_dialog(join_code)


main()