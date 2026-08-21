import streamlit as st
from PIL import Image

@st.dialog("Capture or upload photos")
def add_photos_dialog():
    st.write("Add classroom photos to scan for attendance")

    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab="camera"


    tab1,tab2=st.columns(2)
    with tab1:
        # type1= "primary" if st.session_state.photo_tab == "camera" else "secondary"
        if st.button("Click photo", width="stretch", type="primary"):
            st.session_state.photo_tab="camera"
            

    with tab2:
        # type2= "primary" if st.session_state.photo_tab == "upload" else "secondary"
        if st.button("Upload photos", width="stretch", type="primary"):
            st.session_state.photo_tab="upload"
            
            

    if st.session_state.photo_tab=="camera":
        cam_photo=st.camera_input("Take Snapshot", key="dialog_cam")
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast("Photo Captured!")
            st.rerun()

    if st.session_state.photo_tab=="upload":
        uploaded_files=st.file_uploader("Upload Classroom Photos", type=['jpg','jpeg','png'], accept_multiple_files=True)
        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast("Images uploaded successfully!")
            st.rerun()

    st.divider()
    if st.button("done", type="tertiary", width="stretch"):
        st.rerun()