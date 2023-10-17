"""
Project: Prototyping a Machine Learning Application with Streamlit.
Streamlit app integrated with a pretrained ViT model for image classification.
"""


import streamlit as st
from PIL import Image
import openai
import pandas as pd

# Set the title and caption for the Streamlit app
st.set_page_config(page_title="AI powered Anxiety Management Tool")
openai_api_key = st.sidebar.text_input('OpenAI API Key')
st.title("AI powered Anxiety Management Tool")
image = Image.open('sunrise.jpeg')
st.image(image, caption='Sunrise by the mountains')

def generate_response(input_text):


    openai.api_key = openai_api_key
    
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": "Create a list of JSON object for each day. Each JSON object should have Day, cost effective Activity, Time required "
        },
        {
        "role": "user",
        "content": input_text
        }
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    message = response['choices'][0]['message']['content']
    df = pd.DataFrame.from_dict(eval(message))
    st.dataframe(df)
    return df

def main():
    """
    Main Streamlit function
    """
    with st.form('my_form'):
        prompt = ''

        name = st.text_area('Patient Name:', 'Bruce Wayne')
        prompt+='name: '
        prompt+=name
        prompt+=' .\n'

        learning = st.text_area('Learning Style Information:', 'Bruce is into martial arts')
        prompt+='Learning style: '
        prompt+=learning
        prompt+=' .\n'

        presenting_concerns = st.text_area('Current Concerns:','He is not able to Sleep at night')
        prompt+='Presenting concerns: '
        prompt+=presenting_concerns
        prompt+=' .\n'

        values_systems = st.text_area('Time Money Availiablity:', 'Bruce has his own business and does not have enough time.')
        prompt+='Value systems: '
        prompt+=values_systems
        prompt+=' .\n'

        goals_and_expectation = st.text_area('Goals:','He just wants to be happy')
        prompt+='Goals and Expections: '
        prompt+=goals_and_expectation
        prompt+=' .\n'

        insight = st.text_area('Additional information:','Prepare a chart that helps him to manage stress better weekly for 2 hours within 30 dollar budget')
        prompt+='Insight'
        prompt+=insight
        prompt+=' .'

        submitted = st.form_submit_button('Submit')
        dataframe = pd.DataFrame()

        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            dataframe = generate_response(prompt)
        

if __name__ == "__main__":
    main()
