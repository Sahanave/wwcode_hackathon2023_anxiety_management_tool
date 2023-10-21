# This project uses code from https://github.com/dclin/gptlab-streamlit which is licensed under the MIT License. 
#The original license text can be found https://github.com/dclin/gptlab-streamlit/blob/main/LICENSE.

import streamlit as st 

def st_button(url, label, font_awesome_icon):
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
    button_code = f'''<a href="{url}" target=_blank><i class="fa {font_awesome_icon}"></i>   {label}</a>'''
    return st.markdown(button_code, unsafe_allow_html=True)

def render_linked_in():
  with st.sidebar:
      st.write("Let's connect!")
      st_button(url="https://www.linkedin.com/in/sahana-venkatesh/", label="LinkedIn", font_awesome_icon="fa-linkedin")