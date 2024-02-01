import streamlit as st
import eda 
import prediction

navigasi = st.sidebar.selectbox('Pilih Halaman: ',
                                ('Prediction Model','EDA'))

if navigasi == 'Prediction Model':
    prediction.run()
else:
    eda.run()