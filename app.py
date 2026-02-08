import streamlit as st
from crew import run_crew

from tools.file_reader import read_pdf, read_word, read_csv
from tools.image_processor import extract_text_from_image

# Page configuration
st.set_page_config(
    page_title="AI Workflow Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("🤖 AI Autonomous Workflow Assistant")
st.markdown("### Automate your tasks with intelligent AI agents")
st.divider()

# Main layout (single column for input)
st.subheader("✍️ Task Configuration")

# Task input
task = st.text_area(
    "Describe your task",
    placeholder="Example: Analyze the uploaded document and create a summary report...",
    height=150,
    help="Provide a clear description of what you want the AI to accomplish"
)

# Input options in tabs
tab1, tab2 = st.tabs(["📂 File Upload", "🌐 URL/API"])

with tab1:
    uploaded_file = st.file_uploader(
        "Upload a file",
        type=["pdf", "docx", "csv", "png", "jpg", "jpeg"],
        help="Supported formats: PDF, Word, CSV, Images (PNG, JPG)"
    )
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: **{uploaded_file.name}**")
        st.caption(f"📦 Size: {uploaded_file.size / 1024:.2f} KB")

with tab2:
    url_input = st.text_input(
        "Enter a URL or API endpoint",
        placeholder="https://example.com/data",
        help="Provide a web URL or API endpoint to process"
    )
    if url_input:
        st.success(f"✅ URL provided: **{url_input}**")

st.divider()

# Action buttons
col_btn1, col_btn2 = st.columns([1, 1])
with col_btn1:
    run_button = st.button("▶️ Run Workflow", type="primary", use_container_width=True)
with col_btn2:
    if st.button("🔄 Clear", use_container_width=True):
        st.rerun()

# Run workflow
if run_button:
    if not task.strip():
        st.error("⚠️ Please describe your task before running the workflow.")
    else:
        # Determine input type
        input_data = None
        input_type = "text"

        if uploaded_file is not None:
            input_data = uploaded_file
            if uploaded_file.type == "application/pdf":
                input_data = read_pdf(uploaded_file)
                input_type = "pdf"
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                input_data = read_word(uploaded_file)
                input_type = "word"
            elif "csv" in uploaded_file.type:
                input_data = read_csv(uploaded_file)
                input_type = "csv"
            elif "image" in uploaded_file.type:
                input_data = extract_text_from_image(uploaded_file)
                input_type = "image"
        elif url_input:
            input_data = url_input
            if url_input.startswith("http"):
                input_type = "web"

        # Show progress and run Crew
        with st.spinner("⚙️ AI agents are working on your task..."):
            try:

                
                results = run_crew(task, input_type=input_type, input_data=input_data)
                st.success("🎉 Workflow Completed Successfully!")
                st.divider()

                # Display results
                st.subheader("📈 Results")
                st.markdown(results["crew_output"])

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                with st.expander("🔍 Error Details"):
                    st.code(str(e))

# Footer
st.divider()
st.caption("⚡ Powered by AI Agents | Built with Streamlit")
