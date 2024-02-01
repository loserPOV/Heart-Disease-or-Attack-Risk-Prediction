#import library
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image



def run():
    #set title
    st.markdown("<h1 style='text-align: center; color: grey;'>Welcome to the Exploration Data Analysis (EDA)</h1>", unsafe_allow_html=True)
        
    #set header
    st.markdown("<h2 style='text-align: center; color: grey;'>Halaman ini menampilkan hasil EDA dari dataset heart_disease_health_indicators_BRSFF2015</h2>", unsafe_allow_html=True)

    st.write('----')

    #load dataset
    df = pd.read_csv('deploy.csv')

    st.write('# DataFrame')
    #view dataframe
    st.dataframe(df)
    st.write('---')

    # EDA 1
    st.markdown("<h3 style='text-align: center; color: grey;'>Korelasi Terhadap Heart Disease</h3>", unsafe_allow_html=True)

    image = Image.open('eda1.jpg')
    st.image(image)
    
    
    with st.expander('Explanation'):    
        st.caption("Berdasarkan Heatmap Korelasi setiap fitur dengan target yaitu HeartDiseaseorAttack, Dapat disimpulkan bahwa terdapat beberapa fitur yang memiliki korelasi dengan target. Namun berdasarkan nilai korelasi yang terlihat, tidak ada nilai korelasi yang termasuk besar dengan nilai korelasi terbesar terdapat pada fitur GenHlth (0.26). ")
    st.write('---')

    # EDA 2
    st.markdown("<h3 style='text-align: center; color: grey;'>Distribusi HeartDiseaseorAttack Berdasarkan BMI</h3>", unsafe_allow_html=True)

    image = Image.open('eda2.jpg')
    st.image(image)
    
    with st.expander('Legends'):
        st.caption('- 0 means never diagnosed with heart disease or attack, 1 means have ever diagnosed with heart disease or attack.')
        st.caption('- BMI is Body Mass Index.')
        
    with st.expander('Explanation'):
        st.caption('Berdasarkan distribusi data BMI (Body Mass Index) dan status penyakit jantung (0 untuk tidak ada penyakit jantung dan 1 untuk pernah didiagnosis dengan penyakit jantung), terlihat adanya tren peningkatan BMI seiring bertambahnya nilai BMI, mencapai puncaknya pada sekitar kelompok BMI 27, dan kemudian mengalami penurunan. Korelasi positif antara nilai BMI dan risiko penyakit jantung menunjukkan bahwa individu dengan BMI yang lebih tinggi cenderung memiliki kemungkinan lebih besar untuk mengalami penyakit jantung. Perhatian khusus perlu diberikan pada kelompok BMI sekitar 20 hingga 30, di mana jumlah kasus penyakit jantung tampak signifikan. Temuan ini menyoroti bahwa BMI dapat menjadi faktor penting dalam mengevaluasi risiko penyakit jantung dalam populasi yang dianalisis.')
    st.write('---')

    # EDA 3
    st.markdown("<h3 style='text-align: center; color: grey;'>Distribusi HeartDiseaseorAttack berdasarkan Age Group</h3>", unsafe_allow_html=True)

    image = Image.open('eda3.jpg')
    st.image(image)
    
    with st.expander('Legends'):
        st.caption('- 0 means never diagnosed with heart disease or attack, 1 means have ever diagnosed with heart disease or attack.')
        st.caption('- Age is already grouped from 1 (18 to 24) all the way to 13(80+), 5 year increments.') 
    
    with st.expander('Explanation'):
        st.caption('Visualisasi data tersebut menggambarkan distribusi individu berdasarkan status penyakit jantung dan kelompok usia. Dapat ditarik kesimpulan bahwa terdapat peningkatan signifikan jumlah individu yang pernah didiagnosis dengan penyakit jantung seiring bertambahnya usia, mencapai puncaknya pada kelompok usia 10 (65-69 tahun). Secara umum, jumlah individu tanpa penyakit jantung jauh lebih dominan dalam setiap kelompok usia, tetapi perbandingannya mulai menurun seiring pertambahan usia. Analisis kelompok usia yang lebih muda menunjukkan dominasi individu tanpa penyakit jantung, namun perbandingannya berubah seiring bertambahnya usia. Kesimpulan umum dari data ini adalah bahwa risiko penyakit jantung cenderung meningkat seiring bertambahnya usia, dengan jumlah individu yang memiliki penyakit jantung lebih signifikan pada kelompok usia yang lebih tua.')
    st.write('---')

    # EDA 4
    st.markdown("<h3 style='text-align: center; color: grey;'>Distribusi HeartDiseaseorAttack Berdasarkan Tiap Gender</h3>", unsafe_allow_html=True)

    image = Image.open('eda4.jpg')
    st.image(image)
    
    with st.expander('Legends'):
        st.caption('- 0 means never diagnosed with heart disease or attack, 1 means have ever diagnosed with heart disease or attack.')
        st.caption('- For Sex, 0 means Female, and 1 means male.')
    
    with st.expander('Explanation'):
        st.caption('Visualisasi data tersebut mencerminkan distribusi individu berdasarkan status penyakit jantung dan jenis kelamin. Dapat disimpulkan bahwa jumlah individu tanpa penyakit jantung jauh lebih tinggi dibandingkan dengan yang memiliki penyakit jantung. Analisis lebih lanjut menunjukkan bahwa pada kedua jenis kelamin, jumlah individu tanpa penyakit jantung lebih dominan daripada yang memiliki penyakit jantung. Oleh karena itu, kesimpulan awalnya adalah bahwa jenis kelamin mungkin tidak menjadi faktor penentu utama dalam kejadian penyakit jantung dalam dataset ini.')
    st.write('---')

    # EDA 5
    st.markdown("<h3 style='text-align: center; color: grey;'>Persebaran Data Smoker Berdasarkan Age Group</h3>", unsafe_allow_html=True)

    image = Image.open('eda5.jpg')
    st.image(image)
    
    with st.expander('Legends'):
        st.caption('- 0 means never smoked 100 cigarettes in your entire life, 1 means smoked at least 100 cigarettes in your entire life.')
        st.caption('- Age is already grouped from 1 (18 to 24) all the way to 13(80+), 5 year increments.') 
    
    with st.expander('Explanation'):
        st.caption('Visualisasi tersebut merepresentasikan distribusi individu berdasarkan usia, status perokok, dan jumlah individu dalam setiap kategori. Dari analisis distribusi, dapat diasumsikan bahwa seiring bertambahnya usia, jumlah bukan perokok dan perokok cenderung meningkat, namun mengalami penurunan signifikan setelah kelompok usia 10 (usia 65-69 tahun). Jumlah bukan perokok secara konsisten lebih tinggi kecuali di beberapa kelompok usia tertentu (10, 11, dan 12), menunjukkan bahwa dalam populasi ini, lebih banyak individu bukan perokok daripada perokok. Terdapat kelompok usia tertentu (6, 7, 8, dan 9) dengan tingkat merokok yang relatif lebih tinggi, mungkin menandakan kecenderungan merokok pada kelompok usia tersebut.')
    st.write('---')
    
if __name__ == "__main__":
    run()