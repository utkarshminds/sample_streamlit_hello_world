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
6. Add verification (username and password) code in your python file
7. Write the main project vacation planner code
8. Generate requirements.txt file using
   type in terminal
   pipreqs --ignore venv_folder/ --force
9. commit and sync to github
10. copy secrets.toml contents in 
    settings of streamlit app on streamlit.io
'''
import streamlit as st
import google.generativeai as genai 
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


genai.configure(api_key=st.secrets['API_KEY']['api_key']) #API KEY
model = genai.GenerativeModel("gemini-2.0-flash") #MODEL NAME AND VERSION

budget_data = st.text_input('Enter budget in dollars')
dest_data = st.text_input('Enter destination city')
days_data = st.text_input('Enter number of days')
group_data = st.text_input('Enter group size')
contraints_data = st.text_input('Enter special contraints (food, young or old, hotel type, room type)')

response = model.generate_content(f"""Create a vacation plan based on budget = {budget_data},
                                   destination is {dest_data} for number of days {days_data}
                                  group size {group_data} and consider contraints
                                  {contraints_data}""")
st.write(response.text)


