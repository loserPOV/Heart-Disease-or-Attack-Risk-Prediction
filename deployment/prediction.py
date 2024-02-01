#import library
import pandas as pd
import numpy as np
import streamlit as st

#import pickle
import pickle

#load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    st.markdown("<h1 style='text-align: center; color: grey;'>Model Prediction</h1>", unsafe_allow_html=True)
    st.write('---')

    
    with st.form(key='form parameters'):
        HighBP = st.selectbox('Have you been told to have high blood pressure by a doctor, nurse, or other health professional?', ['No', 'Yes'])
        if HighBP == 'No':
            HighBP = 0
        else:
            HighBP = 1
        
        BMI = st.slider('Input your Body Mass Index', 12, 98, 50)
        
        HighChol = st.selectbox(label='Have you EVER been told by a doctor, nurse or other health professional that your blood cholesterol is high?', options=['No', 'Yes'])
        if HighChol == 'No':
            HighChol = 0
        else:
            HighChol = 1
            
        Smoker = st.selectbox(label='Have you smoked at least 100 cigarettes in your entire life?', options=['No', 'Yes'])
        if Smoker == 'No':
            Smoker = 0
        else:
            Smoker = 1
            
        Stroke = st.selectbox(label='(Ever told) you had a stroke.', options=['No', 'Yes'])
        if Stroke == 'No':
            Stroke = 0
        else:
            Stroke = 1
            
        Diabetes = st.selectbox(label='(Ever told) you have diabetes.', options=['No', 'Yes'])
        if Diabetes == 'No':
            Diabetes = 0
        else:
            Diabetes = 1
            
        GenHlth = st.selectbox(label='Would you say that in general your health is', options=['Excellent', 'Very Good', 'Good', 'Fair', 'Poor'])
        if GenHlth == 'Excellent':
            GenHlth = 1
        elif GenHlth == 'Very Good':
            GenHlth = 2
        elif GenHlth == 'Good':
            GenHlth = 3
        elif GenHlth == 'Fair':
            GenHlth = 4
        else:
            GenHlth = 5
            
        DiffWalk = st.selectbox(label='Do you have serious difficulty walking or climbing stairs?', options=['No', 'Yes'])
        if DiffWalk == 'No':
            DiffWalk = 0
        else:
            DiffWalk = 1
            
        Age = st.selectbox(label='Which age group are you in?', options=['18 to 24', '25 to 29', '30 to 34', '35 to 39', '40 to 44', '45 to 49', '50 to 54', '55 to 59', '60 to 64', '65 to 69', '70 to 74', '75 to 79', '80 or older'])
        if Age == '18 to 24':
            Age = 1
        elif Age == '25 to 29':
            Age = 2
        elif Age == '30 to 34':
            Age = 3
        elif Age == '35 to 39':
            Age = 4
        elif Age == '40 to 44':
            Age = 5
        elif Age == '45 to 49':
            Age = 6
        elif Age == '50 to 54':
            Age = 7
        elif Age == '55 to 59':
            Age = 8
        elif Age == '60 to 64':
            Age = 9
        elif Age == '65 to 69':
            Age = 10
        elif Age == '70 to 74':
            Age = 11
        elif Age == '75 to 79':
            Age = 12
        else:
            Age = 13
            
        Income = st.selectbox(label='In which Income group are your annual household income from all sources?', options=['Less than $10.000', '$10.000 to less than $15.000', '$15.000 to less than $20.000', '$20.000 to less than $25.000', '$25.000 to less than $35.000', '$35.000 to less than $50.000', '$50.000 to less than $75.000', '$75.000 or more'])
        if Income == 'Less than $10.000':
            Income = 1
        elif Income == '$10.000 to less than $15.000':
            Income = 2
        elif Income == '$15.000 to less than $20.000':
            Income = 3
        elif Income == '$20.000 to less than $25.000':
            Income = 4
        elif Income == '$25.000 to less than $35.000':
            Income = 5
        elif Income == '$35.000 to less than $50.000':
            Income = 6
        elif Income == '$50.000 to less than $75.000':
            Income = 7
        else:
            Income = 8
            
        PhysHlth = st.slider('For how many days during the past 30 days was your physical health not good?', 0, 30, 15)

        
        submit = st.form_submit_button('Predict')


    data_inf = {
        'HighBP' : HighBP,
        'BMI' : BMI,
        'HighChol' : HighChol,
        'Smoker' : Smoker,
        'Stroke' : Stroke,
        'Diabetes' : Diabetes,
        'GenHlth' : GenHlth,
        'DiffWalk' : DiffWalk,
        'Age' : Age,
        'Income' : Income,
        'PhysHlth' : PhysHlth
        }
    
    st.write('---')

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submit:
        prediction =  model.predict(data_inf)

        if prediction[0] == 1:
            prediction = 'Anda Memiliki Kemungkinan Terkena Penyakit Jantung atau Serangan Jantung'
        else:
            prediction = 'Kemungkinan Terkena Penyakit Jantung atau Serangan Jantung Kecil'

        st.subheader('Hasil model prediksi adalah :')
        st.subheader(prediction)
        
if __name__ == "__main__":
    run()