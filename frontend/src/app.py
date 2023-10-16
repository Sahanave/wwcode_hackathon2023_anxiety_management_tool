"""
Project: Prototyping a Machine Learning Application with Streamlit.
Streamlit app integrated with a pretrained ViT model for image classification.
"""


import streamlit as st
from PIL import Image
from langchain.llms import OpenAI

# Set the title and caption for the Streamlit app
st.set_page_config(page_title="AI powered Anxiety Management Tool")
openai_api_key = st.sidebar.text_input('OpenAI API Key')
st.title("AI powered Anxiety Management Tool")
image = Image.open('sunrise.jpeg')
st.image(image, caption='Sunrise by the mountains')
openai_api_key = 'Dummy'

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

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
            generate_response(prompt)


if __name__ == "__main__":
    main()
