from supabase import Client, create_client
import streamlit as st

supabase: Client=create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

