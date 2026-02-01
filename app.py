import streamlit as st

st.set_page_config(page_title="AI Autonomous Workflow Assistant", layout="wide")

st.title("🧠 AI Autonomous Workflow Assistant")
st.write("Give me a task, and I’ll figure out how to do it.")

task = st.text_area("Enter your task:")

if st.button("Run Workflow"):
    st.success("Workflow will start here 🚀")
    st.write("Task received:", task)
