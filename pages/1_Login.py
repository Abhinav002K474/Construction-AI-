import streamlit as st

st.title("Login to Bidflow AI")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email == "admin@bidflow.ai" and password == "admin123":
        st.session_state.user = email
        st.session_state.role = "admin"
        st.success("Admin Login Successful")
    elif email == "user@bidflow.ai" and password == "user123":
        st.session_state.user = email
        st.session_state.role = "user"
        st.success("User Login Successful")
    else:
        st.error("Invalid credentials")
