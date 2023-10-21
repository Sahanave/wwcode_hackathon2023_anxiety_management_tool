"""
1. This project uses code from https://github.com/dclin/gptlab-streamlit which is licensed under the MIT License.  
The original license text can be found https://github.com/dclin/gptlab-streamlit/blob/main/LICENSE.
"""

import streamlit as st
from backend.therapist_dashboard import validate_open_api_key, fetch_user_names, run_setup
from frontend.new_patient import new_patient_form
from frontend.session_page import new_session


st.set_page_config(page_title="AI powered Anxiety Management Tool")
st.title("AI powered Anxiety Management Tool")

def view_get_info():
    user_key_prompt = "Enter your OpenAI API key to get started. Keep it safe, as it'll be your key to coming back. For more information on OpenAI API rate limits, check [this link](https://platform.openai.com/docs/guides/rate-limits/overview).\n\n- Don't have an API key? No worries! Create one [here](https://platform.openai.com/account/api-keys).\n- Want to upgrade your free-trial API key? Just enter your billing information [here](https://platform.openai.com/account/billing/overview)."
    api_key_placeholder = "Paste your OpenAI API key here (sk-...)"
    st.info(user_key_prompt)
    st.text_input("Enter your OpenAI API Key", key="user_key_input",on_change=validate_open_api_key, type="password", autocomplete="current-password", placeholder=api_key_placeholder)

def choose_patient():
    # Some default options
    options = fetch_user_names() + ['new patient']
    new_patient = False

    # Dropdown
    choice = st.selectbox('Choose an option:', options)

    # If 'Other' is selected, show a text input
    if choice == 'new patient':
        new_patient = True
        other_option = st.text_input('Please specify:')
        if other_option:
            st.write(f'You chose: {other_option}')
    else:
        st.write(f'You chose: {choice}')
    return new_patient, choice


def main():
    """
    Main Streamlit function
    """
    view_get_info()
    if 'valid_key' in st.session_state and st.session_state['valid_key']:
        run_setup()
        prompt = ''

        new_patient, choice = choose_patient()
        if new_patient:
            new_patient_form(choice)
        else:
            demo_info = {'name': 'Bruce'}
            new_session()


    
       


if __name__ == "__main__":
    main()
