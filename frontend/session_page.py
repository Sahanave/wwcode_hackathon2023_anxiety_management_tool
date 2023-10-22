
from backend.therapist_dashboard import generate_response
from setup.database import get_patients_previous_sessions, insert_into_session


def new_session(demo_info):
    import streamlit as st
    other_button = st.button('Previous sessions')

    if other_button:
            previous_sessions = get_patients_previous_sessions(demo_info['name'])
            st.dataframe(previous_sessions)

    with st.form('my_form'):
                session_info = {}
                
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
                    response = generate_response(prompt,openai_api_key)
                    demo_info['activity'] = response.to_json()
                    insert_into_session(demo_info)
                    st.dataframe(response)

