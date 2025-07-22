import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def eda():
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis (EDA)</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    # Load dataset
    df = pd.read_csv('diabetes_data_upload.csv')

     # Membagi data positif dan negatif
    df_positif = df[df['class'] == 'Positive']
    df_negatif = df[df['class'] == 'Negative']

    # Pilihan analisis di scroll box
    analysis_options = [
        "1. Statistik Umur Penderita Diabetes",
        "2. Pengaruh pasien yang positif diabetes dengan penyembuhan luka yang lambat",
        "3. Hubungan obesitas dengan positif diabetes",
        "4. Pengaruh umur terhadap penyembuhan luka",
        "5. Melihat Orang yang positif diabetes tapi tanpa gejala",
        "6. Jumlah orang yang positif diabetes mengalami gejala Polyuria dan Polydipsia",
        "7. Gejala yang paling sering ditemui saat terindikasi positif diabetes"
    ]

    choice = st.selectbox("Pilih Analisis EDA:", analysis_options)

    if choice == "1. Statistik Umur Penderita Diabetes":
        st.markdown("## Statistik Umur Penderita Diabetes (Class = Positive)")
        df_positif = df[df['class'] == 'Positive']

        age_mean = df_positif['Age'].mean()
        age_max = df_positif['Age'].max()
        age_min = df_positif['Age'].min()
        age_median = df_positif['Age'].median()

        stats = ['Rata-rata Umur', 'Umur Tertua', 'Umur Termuda', 'Umur Median']
        values = [age_mean, age_max, age_min, age_median]

        fig, ax = plt.subplots(figsize=(9, 6))
        bars = ax.bar(stats, values, color=['#87CEEB', '#90EE90', '#FA8072', '#FFA500'], width=0.5)

        ax.set_title('Statistik Umur Penderita Diabetes', fontsize=16, weight='bold')
        ax.set_ylabel('Umur (tahun)', fontsize=14)
        ax.set_ylim(0, max(values) + 10)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{round(height)}', ha='center', va='bottom', fontsize=12)

        st.pyplot(fig)

        st.markdown("## Kesimpulan")
        st.markdown("""
        1. Rata-rata penderita diabetes ada di umur 39 tahun sampai 58 tahunan.
        2. Ada beberapa pasien penderita diabetes yang sudah tua, yaitu di umur 79 sampai 90 tahun.
        """)

    elif choice == "2. Pengaruh pasien yang positif diabetes dengan penyembuhan luka yang lambat":
        st.markdown("## Pengaruh Diabetes terhadap Penyembuhan Luka")
        delayed_healing_counts = df_positif['delayed healing'].value_counts().reset_index()
        delayed_healing_counts.columns = ['delayed healing', 'Count']
        
        fig = px.bar(
                delayed_healing_counts,
                x='delayed healing',
                y='Count',
                color='delayed healing',
                color_discrete_map={'Yes': 'red', 'No': 'green'},
                labels={'delayed healing': 'Penyembuhan Lambat', 'Count': 'Jumlah Pasien'},
                template='plotly_white' 
        )
        fig.update_layout(
            font_size=14,        # Ukuran font yang nyaman dibaca
            margin=dict(l=80, r=80, t=100, b=120),  # Margin yang cukup agar tidak terpotong
            showlegend=False,    # Sembunyikan legenda karena warna sudah jelas
            height=700,          # Tinggi grafik yang pas
            width=600            # Lebar grafik yang pas
        )
        st.plotly_chart(fig)

        st.markdown("## Kesimpulan")
        st.markdown("""
        Delayed Healing bukan satu-satu faktor untuk melihat bahwa pasien positif diabetes
        """)

    elif choice == "3. Hubungan obesitas dengan positif diabetes":
        st.markdown("## Hubungan Obesitas dengan Diabetes")
        obesity_pos_counts = df_positif['Obesity'].value_counts().reset_index()
        obesity_neg_counts = df_negatif['Obesity'].value_counts().reset_index()

        obesity_pos_counts['Status'] = 'Positive'
        obesity_neg_counts['Status'] = 'Negative'
        combined = pd.concat([obesity_pos_counts, obesity_neg_counts])
        combined.columns = ['Obesity', 'Count', 'Status']

        fig = px.bar(
            combined,
            x='Obesity',
            y='Count',
            color='Status',
            barmode='group',
            color_discrete_map={'Positive': 'red', 'Negative': 'green'},
            labels={'Obesity': 'Obesitas', 'Count': 'Jumlah Pasien'}
        )
        fig.update_layout(
            font_size=14,        # Ukuran font yang nyaman dibaca
            margin=dict(l=80, r=80, t=100, b=120),  # Margin yang cukup agar tidak terpotong
            showlegend=False,    # Sembunyikan legenda karena warna sudah jelas
            height=700,          # Tinggi grafik yang pas
            width=600            # Lebar grafik yang pas
        )
        st.plotly_chart(fig)
        st.markdown("## Kesimpulan")
        st.markdown("""
          Tidak selalu orang yang obesitas akan terdeteksi positif diabetes tahap awal.
        """)
       

    elif choice == "4. Pengaruh umur terhadap penyembuhan luka":
        st.markdown("## Pengaruh Umur terhadap Penyembuhan Luka")
        df['Delayed_Healing_Numeric'] = df['delayed healing'].map({'No': 0, 'Yes': 1})

        fig = px.scatter(
            df,
            x='Age',
            y='Delayed_Healing_Numeric',
            trendline="lowess",
            title='Hubungan Umur dengan Delayed Healing',
            labels={'age': 'Umur', 'Delayed_Healing_Numeric': 'Penyembuhan Lambat (0=No, 1=Yes)'},
            color='class',
            color_discrete_map={'Positive': 'red', 'Negative': 'green'},
        )

        fig.update_layout(
            font_size=14,        # Ukuran font yang nyaman dibaca
            margin=dict(l=80, r=80, t=100, b=120),  # Margin yang cukup agar tidak terpotong
            showlegend=False,    # Sembunyikan legenda karena warna sudah jelas
            height=700,          # Tinggi grafik yang pas
            width=700            # Lebar grafik yang pas
        )
        st.plotly_chart(fig)

        st.markdown("## Kesimpulan")
        st.markdown("""
          Semakin tua umur semakin beresiko penyembuhan lukanya melambat, jadi belum tentu yang penyembuhan lukanya melambat terindikasi diabetes.
        """)

    elif choice == "5. Melihat Orang yang positif diabetes tapi tanpa gejala":
        st.markdown("## Pasien Positif Diabetes Tanpa Gejala")
        gejala_cols = [
            'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness',
            'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching',
            'Irritability', 'delayed healing', 'partial paresis',
            'muscle stiffness', 'Alopecia', 'Obesity'
        ]

        def count_yes(row):
            return sum(row[col] == 'Yes' for col in gejala_cols)

        df_positif['Total_Gejala'] = df_positif.apply(count_yes, axis=1)

        tanpa_gejala_count = df_positif[df_positif['Total_Gejala'] == 0].shape[0]
        dengan_gejala_count = df_positif[df_positif['Total_Gejala'] > 0].shape[0]

        counts = [tanpa_gejala_count, dengan_gejala_count]
        labels = ['Tanpa Gejala', 'Dengan Gejala']

        fig = px.bar(
            x=labels,
            y=counts,
            color=labels,
            color_discrete_map={'Tanpa Gejala': 'red', 'Dengan Gejala': 'orange'},
            title='Jumlah Pasien Positif Diabetes Berdasarkan Kehadiran Gejala',
            labels={'x': 'Kehadiran Gejala', 'y': 'Jumlah Pasien'}
        )
        st.plotly_chart(fig)

        st.markdown("## Kesimpulan")
        st.markdown("""
          Ada juga pasien yang positif diabetes tapi tanpa gejala, walaupun jumlahnya sedikit
        """)

    elif choice == "6. Jumlah orang yang positif diabetes mengalami gejala Polyuria dan Polydipsia":
        st.markdown("## Pasien Positif Diabetes dengan Gejala Polyuria dan Polydipsia")
        total_positif = df_positif.shape[0]
        polyuria_polydipsia_count = df_positif[
            (df_positif['Polyuria'] == 'Yes') & (df_positif['Polydipsia'] == 'Yes')
        ].shape[0]

        st.write(f"Jumlah Pasien positif diabetes dengan gejala Polyuria dan Polydipsia adalah **{polyuria_polydipsia_count}** dari **{total_positif}** pasien.")

        fig = px.bar(
            x=['Polyuria & Polydipsia', 'Lainnya'],
            y=[polyuria_polydipsia_count, total_positif - polyuria_polydipsia_count],
            color=['Polyuria & Polydipsia', 'Lainnya'],
            color_discrete_map={'Polyuria & Polydipsia': 'red', 'Lainnya': 'lightgreen'},
            title='Pasien dengan Polyuria dan Polydipsia',
            labels={'x': 'Kategori', 'y': 'Jumlah Pasien'}
        )
        st.plotly_chart(fig)

        st.markdown("## Kesimpulan")
        st.markdown("""
          Poyuria dan Polydipsia menjadi salah dua gejala yang menandakan pasien positif diabetes
        """)

    elif choice == "7. Gejala yang paling sering ditemui saat terindikasi positif diabetes":
        st.markdown("## Frekuensi Gejala pada Pasien Positif Diabetes")
        gejala_cols = [
            'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness',
            'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching',
            'Irritability', 'delayed healing', 'partial paresis',
            'muscle stiffness', 'Alopecia', 'Obesity'
        ]

        frekuensi_gejala = df_positif[gejala_cols].apply(lambda x: (x == 'Yes').sum()).sort_values(ascending=False)

        fig = px.bar(
            x=frekuensi_gejala.index,
            y=frekuensi_gejala.values,
            color=frekuensi_gejala.values,
            color_continuous_scale='Reds',
            title='Frekuensi Gejala pada Pasien Positif Diabetes',
            labels={'x': 'Gejala', 'y': 'Jumlah Pasien dengan Gejala'}
        )
        fig.update_layout(xaxis_tickangle=45)
        st.plotly_chart(fig)

        st.markdown("## Kesimpulan")
        st.markdown("""
        5 gejala yang paling tinggi atau sering muncul pada pasien positif diabetes
                    
        1. polyuria (kondisi sering buang air kecil) = 243 pasien
        2. polydipsia (rasa haus yang berlebihan) =  225 pasien
        3. weakness (kondisi fisik yang melemah) = 218 pasien
        4. partial paresis (melemah atau lumpuhnya otot) = 192 pasien 
        5. polypaghia (rasa lapar atau nafsu makan yang berlebihan) = 189 pasien
                    
        Gejala obesitas menjadi gejala yang paling rendah bagi orang yang positif diabetes

           
        """)    
        
if __name__ == '__main__':
    eda()