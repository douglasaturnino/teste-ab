import os
import time
import requests
import streamlit as st

class sidebar:
    def __init__(self):
        if 'comecar' not in st.session_state:
            st.session_state.comecar = False
        
        if 'apagar' not in st.session_state:
            st.session_state.apagar = False

        self.sidebar()

    def sidebar(self):
        st.title('Opções')
        
        def comecar():
            st.session_state.comecar = not st.session_state.comecar
        
        def apagar():
            st.session_state.apagar = not st.session_state.apagar
        
        st.write('Click no botão começar para iniciar o experimento:')
        st.button('Começar', on_click=comecar)
        
        st.write('Click no botão para apagar o experimento :')
        st.button('Apagar', on_click=apagar)
        
        
        if st.session_state.comecar:
            url = os.getenv('WEBSCRAPER_URL')
            r = requests.get(url)
            st.session_state.comecar = False
            time.sleep(1)
        
        if st.session_state.apagar:
            url = os.getenv('WEB_URL')
            url = url + '/apagar'
            r = requests.get(url)
            st.write(r.text)
            st.session_state.apagar = False
            time.sleep(1.5)