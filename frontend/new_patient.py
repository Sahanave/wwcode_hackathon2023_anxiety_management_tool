import setup.database as setup_db
from frontend.session_page import new_session

def new_patient_form(name):
    import streamlit as st

    with st.form('new_patient_form'):
            input_json = {}
            input_json['name'] = name

            st.markdown("## Demographics")
            
            age = st.text_area('Age:', '0')
            input_json['age'] = int(age)

            city = st.text_area('City:', 'Goutham')
            input_json['city'] = city

            languages = st.text_area('languages spoken:', 'English')
            input_json['languages'] = languages

            academic_background = st.text_area('academic_background:', 'Graduate')
            input_json['academics'] = academic_background

            family = st.text_area('Family:', 'brother')
            input_json['family'] = family

            submitted = st.form_submit_button('Submit')
            if submitted:
                  setup_db.insert_into_patients(input_json)
                  new_session(input_json)
