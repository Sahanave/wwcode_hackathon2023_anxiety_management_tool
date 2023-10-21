"""
1. This project uses code from https://github.com/dclin/gptlab-streamlit which is licensed under the MIT License.  
The original license text can be found https://github.com/dclin/gptlab-streamlit/blob/main/LICENSE.
"""

import streamlit as st
from PIL import Image
from backend.src.threapist_dashboard import generate_response, fetch_user_names
st.set_page_config(page_title="AI powered Anxiety Management Tool")
openai_api_key = st.sidebar.text_input('OpenAI API Key')
st.title("AI powered Anxiety Management Tool")
image = Image.open('sunrise.jpeg')
st.image(image, caption='Sunrise by the mountains')
openai_api_key = 'Dummy'

def main():
    """
    Main Streamlit function
    """
    with st.form('my_form'):
        prompt = ''

        name = st.text_area('Patient Name:', 'Bruce Wayne')
        prompt+=name
        prompt+=' .'

        background_info = st.text_area('Intake and Background Information:', 'Bruce lost his parents in a young age')
        prompt+=background_info
        prompt+=' .'

        presenting_concerns = st.text_area('Current Concerns:','He is not able to Sleep at night')
        prompt+=presenting_concerns
        prompt+=' .'

        values_systems = st.text_area('Values and Beliefs:', 'Bruce believes in serving justice')
        prompt+=values_systems
        prompt+=' .'

        goals_and_expectation = st.text_area('Goals:','He just wants to be happy')
        prompt+=goals_and_expectation
        prompt+=' .'

        insight = st.text_area('Additional information:','Prepare a chart that helps him to manage stress better')
        prompt+=insight
        prompt+=' .'

        submitted = st.form_submit_button('Submit')

        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(prompt,openai_api_key)


if __name__ == "__main__":
    main()
