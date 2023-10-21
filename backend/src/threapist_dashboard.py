import sqlite3
import pandas as pd
import openai


def generate_response(input_text, openai_api_key):


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
    return df

def fetch_user_names():
    conn = sqlite3.connect('aitool.db')
    query = '''
            Select district name FROM create_demographics_table;
            '''
    patitents = pd.read_sql(query, conn)
    if patitents.empty:
        return None
    else:
        return patitents['name'].tolist()


def update_data(query, parameters):
    with conn:
        cur = conn.cursor()
        cur.execute(query, parameters)