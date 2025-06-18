import streamlit as st
import home, eda, predict

with st.sidebar:

    st.title("Projek Deteksi Diabetes Tahap Awal")
    st.write('## Pilih Halaman')
    navigation = st.radio('Page', ['Home','EDA', 'Tools Prediksi Diabetes'])
    
    st.write("# About")
    st.markdown('Proyek ini adalah proyek untuk pembuatan machine learning dalam mendeteksi Diabetes Tahap Awal ') 

    
if navigation == "Home":
    home.home()
elif navigation == "EDA":
    eda.eda()
elif navigation == "Tools Prediksi Diabetes" :
    predict.predict()


