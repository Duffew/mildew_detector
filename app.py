import streamlit as st
from app_pages.page_manager import PageManager

st.title("🚀 Mildew Detection Dashboard")
st.write("Welcome to the Streamlit dashboard for analyzing mildew detection!")

if st.button("Run Analysis"):
    st.write("⚙️ Processing... (Coming soon!)")

app = PageManager()
app.run()