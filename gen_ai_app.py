'''
Vacation planner
Day planner
Resume suggestions
Prepration for job interview
Notes study preparation

Things we need:
1. Streamlit for user interface
2. Generative AI API KEY
3. Prompt

Steps
=====
1. Create a folder .streamlit
2. Create a file inside .streamlit folder as 
    secrets.toml
3. Write in secrets.toml
   [GOOGLE_API_KEY]
   api_key = 'PASTE YOUR API KEY'
4. write .gitignore
    .streamlit/
    secrets.toml
    *.toml
5. To add login 
    write / copy in secrets.toml
    [passwords]
    pranav = "pranav123"
    raju = 'raju123'
    username = "password"
6. Add verification code in your python file
'''
import streamlit as st

#VERIFICATION CODE STARTS
import hmac

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()
#VERIFICATION CODE ENDS

st.title('Vacation planner using Gen AI')



