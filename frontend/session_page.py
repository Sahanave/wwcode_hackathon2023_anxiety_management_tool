
from backend.therapist_dashboard import generate_response

def new_session(demo_info):
    import streamlit as st
    with st.form('my_form'):
                prompt = str(demo_info)
                prompt+=' '
                
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
                
                if submitted:
                    openai_api_key = st.session_state["user_key_input"]
                    generate_response(prompt,openai_api_key)