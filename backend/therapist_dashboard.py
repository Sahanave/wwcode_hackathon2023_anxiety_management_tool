import sqlite3
import pandas as pd
import openai
import streamlit as st
import setup.database as setup_db

def run_setup():
    setup_db.main()


def validate_open_api_key():
    openai_api_key = '123'
    if 'user_key_input' in st.session_state.keys():
        openai_api_key = st.session_state["user_key_input"]
    try:
        #generate_response('dummy', openai_api_key, 'gpt-3.5-turbo')
        x = 1+2
    except Exception as ex:
        st.session_state['valid_key'] = False
        st.warning(f"Something went wrong. Invalid key.{ex}")  
    else:
        st.session_state['valid_key'] = True

def generate_response(input_text, openai_api_key, model="gpt-4"):


    openai.api_key = openai_api_key
    
    response = openai.ChatCompletion.create(
    model=model,
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
    return df

def fetch_user_names():
    conn = sqlite3.connect('aitool.db')
    query = '''
            Select DISTINCT name FROM patients;
            '''
    patitents = pd.read_sql(query, conn)
    conn.close()
    if patitents.empty:
        options = []
    else:
       options = patitents['name'].tolist()
    return options

def get_user_entry(name):
    conn = sqlite3.connect('aitool.db')
    query = f'''
            Select * FROM patients where name = '{name}';
            '''
    patient = pd.read_sql(query, conn).iloc[-1].to_dict()
    return patient
