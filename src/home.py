import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

def home():
    #isi page

    #title
    st.markdown("<h1 style='text-align: center; white-space: nowrap;'>MENDETEKSI DIABETES TAHAP AWAL</h1>", unsafe_allow_html=True)


    image_url = 'src/Banner.jpg'
    gambar = Image.open(image_url)
    st.image(gambar)

    st.markdown("<hr>", unsafe_allow_html=True)

    #deskripsi

    st.markdown(
        """
        <div style='text-align: justify;'>
        Konsumsi gula berlebihan menjadi masalah kesehatan serius yang sering terabaikan. 
        Hal ini bisa dijumpai di berbagai usia karena mudahnya akses ke makanan dan minuman manis di berbagai tempat seperti supermarket, minimarket, warung-warung, dan gerobak jajanan pinggir jalan. Kondisi ini sangat mengkhawatirkan karena konsumsi gula secara terus-menerus dapat meningkatkan risiko diabetes.  
        Diabetes merupakan salah satu penyebab kematian tertinggi di dunia. Deteksi dini diabetes sangat penting agar risiko komplikasi dapat diminimalisir. Dengan adanya deteksi dini pada masyarakat, tenaga medis, orang tua, dan keluarga dapat melakukan pencegahan risiko yang lebih parah di masa depan. Oleh karena itu, diperlukan metode deteksi dini diabetes untuk membantu orangtua, keluarga, dan tenaga medis dalam pencegahan risiko yang lebih serius serta penanganan lebih awal.
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("## Problem Statement")

    st.markdown(
        """
        <div style='text-align: justify;'>
        Melakukan pembuatan machine learning untuk mendeteksi gejala dini diabetes pada masyarakat, sehingga dapat membantu tenaga medis, orang tua, dan keluarga melakukan pencegahan resiko kompilasi yang lebih parah di masa depan.
        </div>
        """, 
        unsafe_allow_html=True
    )

    #EDA

    st.markdown("## Dataset")
    st.markdown('Dataset diambil dari archive.ics.uci.edu dengan isi umur, gender, dan gejala-gejala yang terindikasi diabetes')

    #Menampilkan data frame
    df = pd.read_csv('diabetes_data_upload.csv')
    st.dataframe(df)

    #Menampilkan keterangan data frame

    # Data tabel dalam bentuk dictionary
    data = {
        "Nama Kolom": [
            "Age", "Gender", "Polyuria", "Polydipsia", "Sudden weight loss", "Weakness",
            "Polyphagia", "Genital thrush", "Visual blurring", "Itching", "Irritability",
            "Delayed healing", "Partial paresis", "Muscle stiffness", "Alopecia", "Obesity", "Class"
        ],
        "Keterangan": [
            "Usia pasien",
            "Jenis kelamin pasien (Female = perempuan, Male = laki-laki)",
            "Kondisi sering buang air kecil, gejala umum diabetes",
            "Rasa haus yang berlebihan",
            "Penurunan berat badan secara tiba-tiba",
            "Kondisi fisik yang melemah",
            "Rasa lapar atau nafsu makan yang berlebihan",
            "Infeksi jamur pada area genital",
            "Penglihatan yang kabur",
            "Rasa gatal pada anggota badan",
            "Mudah marah atau gelisah",
            "Luka yang lama sembuhnya",
            "Kelemahan atau kelumpuhan sebagian otot",
            "Kekakuan pada otot",
            "Kebotakan atau rambut yang rontok",
            "Kegemukan",
            "Hasil diagnosis diabetes (Positive = terdiagnosis diabetes)"
        ]
    }

    # Membuat DataFrame dari data
    df = pd.DataFrame(data)

    # Menampilkan judul
    st.title("Keterangan Nama-nama Kolom")

    # Menampilkan tabel
    st.table(df)

if __name__ == '__main__' :
    home()
