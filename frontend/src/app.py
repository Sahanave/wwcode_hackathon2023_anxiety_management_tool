"""
Project: Prototyping a Machine Learning Application with Streamlit.
Streamlit app integrated with a pretrained ViT model for image classification.
"""


import streamlit as st
from PIL import Image
   
def main():
    """
    Main Streamlit function
    """

    # Set the title and caption for the Streamlit app
    st.set_page_config(page_title="AI powered Anxiety Management Tool")
    st.title("AI powered Anxiety Management Tool")
    image = Image.open('sunrise.jpeg')
    st.image(image, caption='Sunrise by the mountains')
    with st.form('my_form'):

        name = st.text_area('Patient Name:', 'Bruce Wayne')
        background_info = st.text_area('Intake and Background Information:', 'Bruce lost his parents in a young age')
        presenting_concerns = st.text_area('Current Concerns:','He is not able to Sleep at night')
        values_systems = st.text_area('Values and Beliefs:', 'Bruce believes in serving justice')
        goals_and_expectation = st.text_area('Goals:','He just wants to be happy')
        insight = st.text_area('Additional information:','Prepare a chart that helps him to manage stress better')
        submitted = st.form_submit_button('Submit')


if __name__ == "__main__":
    main()
