import os
import time
import requests 
import streamlit as st
import pandas as pd
from analytics_bayesian import get_chart_data
from sidebar import sidebar

with st.sidebar.container():
    sidebar()

chart_data = pd.DataFrame()
mensagem = st.title('')
chart = st.line_chart()
max_x = 50

with st.container():
    while True:
        max_data = len(chart_data) - max_x
    
        try:
            chart_data = get_chart_data()
            mensagem.title('Probabilidade de B ser melhor que A')
        except IndexError:
            mensagem.title('Não existe valores para gerar o grafico')
    
        chart.line_chart(chart_data)
        time.sleep(2)

        if max_data == len(chart_data) - max_x:
            break
    