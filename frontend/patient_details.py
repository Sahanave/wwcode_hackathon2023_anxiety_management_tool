import setup.database as setup_db

def patient_form(input_json):
    import streamlit as st

    with st.form('patient_form'):

            st.markdown("## Demographics")
            
            age = st.text_area('Age:', input_json['age'])
            input_json['age'] = int(age)

            city = st.text_area('City:', input_json['city'])
            input_json['city'] = city

            languages = st.text_area('languages spoken:', input_json['languages'])
            input_json['languages'] = languages

            academic_background = st.text_area('academic_background:', input_json['academics'])
            input_json['academics'] = academic_background

            family = st.text_area('Family:', input_json['family'])
            input_json['family'] = family

            submitted = st.form_submit_button('Submit')
            if submitted: 
                  setup_db.insert_into_patients(input_json)
    
    return input_json
