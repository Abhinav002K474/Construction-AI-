import streamlit as st

# Page config
st.set_page_config(
    page_title="Bidflow AI",
    page_icon="⚡",
    layout="wide"
)

# Main UI
st.title("⚡ Bidflow AI")
st.subheader("AI Electrical Estimation Platform")

st.success("Streamlit is running successfully")

# Test upload
st.divider()

st.header("Test PDF Upload")

uploaded_file = st.file_uploader(
    "Upload Electrical Estimate PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
