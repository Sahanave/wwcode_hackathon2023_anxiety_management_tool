
from backend.therapist_dashboard import generate_response
import setup.database as get_patients_previous_sessions


def new_session(demo_info):
    import streamlit as st
    with st.form('my_form'):
                session_info = {}

                other_button = st.button('Previous sessions')

                if other_button:
                       st.dataframe(get_patients_previous_sessions(demo_info['name']))
                
                learning = st.text_area('Preferred Learning (Art, Yoga, Writing(please provide prompt idea)):', 'None')
                session_info['learning'] = learning

                availability_time = st.text_area('Availability :','None')
                session_info['availability_time'] = availability_time

                weekly_budget = st.text_area('Budget:','0 dollars')
                session_info['weekly_budget'] = weekly_budget

                insight = st.text_area('Additional information:','Prepare a chart that helps him to manage stress better')
                session_info['insight'] = insight

                submitted = st.form_submit_button('Submit')
                
                if submitted:
                    openai_api_key = st.session_state["user_key_input"]

                    demo_info.update(session_info)
                    prompt = str(demo_info)
                    st.dataframe(generate_response(prompt,openai_api_key))