import streamlit as st
import segno
import io

@st.dialog("Share class link")
def share_subject_dialog(name,code):
    app_domain="presenceai-main.streamlit.app"
    join_url=f"{app_domain}/?join-code={code}"

    st.subheader("Join class using link/QR")
    qr=segno.make(join_url)
    out=io.BytesIO()
    qr.save(out, kind="png", scale=10, border=1)

    c1,c2=st.columns(2)
    with c1:
        st.markdown("### copy link")
        st.code(f"{join_url}", language="text")
        st.code(f"{code}", language="text")
        st.info("Copy this URL to share on whatsapp or email!")

    with c2:
        st.markdown("### Scan QR")
        st.image(out.getvalue(), caption="QR code for join class")