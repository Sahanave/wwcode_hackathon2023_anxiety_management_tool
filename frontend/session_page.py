
from backend.therapist_dashboard import generate_response

def new_session(demo_info):
    import streamlit as st
    with st.form('my_form'):
                
                learning = st.text_area('Preferred Learning (Art, Yoga, Writing(please provide prompt idea)):', 'None')
                demo_info['learning'] = learning

                availability_time = st.text_area('Availability :','None')
                demo_info['availability_time'] = availability_time

                weekly_budget = st.text_area('Budget:','0 dollars')
                demo_info['weekly_budget'] = weekly_budget

                insight = st.text_area('Additional information:','Prepare a chart that helps him to manage stress better')
                demo_info['insight'] = insight

                submitted = st.form_submit_button('Submit')
                
                if submitted:
                    openai_api_key = st.session_state["user_key_input"]
                    prompt = str(demo_info)
                    st.dataframe(generate_response(prompt,openai_api_key))