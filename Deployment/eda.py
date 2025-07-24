import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def eda():
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis (EDA)</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    # Load dataset
    df = pd.read_csv('Deployment/diabetes_data_upload.csv')

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
        <div style="text-align: justify;">
                    1. Rata-rata umur yang positif diabetes ada di 49 dan mediannya di 48<br>
                    2. Umur minimum yang positif diabetes ada di angka 16 tahun, berarti walaupun rata-rata di umur 48 tahun, diabetes juga bisa muncul di usia muda
                    3. Umur maksimum penderita diabetes adalah 90 tahun, menunjukkan bahwa pasien lansia juga masih berisiko terkena diabetes tahap awal. Hal ini mendukung pentingnya skrining rutin untuk semua kelompok umur, termasuk lansia

        Hal ini juga sesuai dengan literatur medis dimana disebutkan bahwa resiko diabetes meningkat seiring bertambahnya usia, terutama jika di atas 40 tahun. 
        Namun dari data di atas terlihat fakta bahwa ada pasien dengan usia muda, yaitu 16 tahun. Itu menunjukkan bahwa ada faktor resiko lain (seperti genetik dan pola makan) juga berperan dalam munculnya diabetes di usia muda<br><br>

        Referensi: <a href="https://www.cdc.gov/diabetes/about/?CDC_AAref_Val=https://www.cdc.gov/diabetes/basics/diabetes.html" target="_blank">CDC - Diabetes Basics</a>
        </div>
        """, unsafe_allow_html=True)


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
                    <div style="text-align: justify;">
                            Dari diagram di atas bisa diambil kesimpulan bahwa pada diabetes tahap awal, Delayed Healing bukan satu-satunya faktor untuk melihat bahwa pasien positif diabetes.
                            Pada tahap awal, kadar gula darah mungkin belum cukup tinggi untuk memengaruhi regenerasi jaringan secara signifikan.
                            Gejala ini biasanya lebih jelas pada fase diabetes lanjut karena **kerusakan kapiler darah dan sistem imun yang melemah.

                            Referensi: [Halodoc - Ini Alasan Luka Lebih Susah Sembuh pada Pengidap Diabetes](https://www.halodoc.com/artikel/ini-alasan-luka-lebih-susah-sembuh-pada-pengidap-diabetes)</a>
                    </div>
                    """, unsafe_allow_html=True)

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
          Tidak selalu orang yang obesitas akan terdeteksi positif diabetes tahap awal. Walaupun obesitas adalah faktor risiko diabetes tipe 2, tidak semua penderita diabetes tahap awal adalah obesitas. Hal ini dapat disebabkan oleh faktor keturunan, resistensi insulin, atau gaya hidup lain yang berisiko, bahkan pada individu dengan berat badan normal juga bisa terindikasi diabetes.  

Referensi : [aido.id - obesitas menjadi faktor pemicu diabetes](https://aido.id/health-articles/obesitas-menjadi-faktor-pemicu-penyakit-diabetes/detail)
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
          Dari line plot di atas juga menguatkan ada **hubungan linear antara umur dan delay healing.** Semakin bertambahnya usia (sumbu x) semakin beresiko mengalami delay healing (sumbu y). Itu terlihat dari line yang terus meningkat perlahan sejalan dengan umur pasien yang bertambah. Maka wajar jika pasien lansia lebih rentan mengalami luka yang lambat sembuh, tidak hanya karena diabetes. Berdasarkan hasil dari **Cohen's d, kekuatan hubungannya sedang**, jadi ada faktor lain yang mempengaruhi delay healing selain umur. Maka dari itu bisa jadi kesimpulan juga **bukan hanya positif diabetes yang menyebabkan penyembuhan luka lambat, tapi umur juga berpengaruh.**

Referensi : [kumparanmom : masa otot menurun sejak usia 30 an](https://kumparan.com/kumparanmom/massa-otot-menyusut-sejak-usia-30-tahun-yuk-perhatikan-ini-moms-23F2kz3V66p)
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
          Dari diagram di atas bisa saya simpulkan ternyata ada juga pasien yang **positif diabetes tanpa gejala,** tapi jumlahnya sangat **sedikit sekali.** Ini menunjukkan adanya kasus **asymptomatic diabetes di tahap awal.** Hal ini sering terjadi, terutama pada pasien yang tidak sadar akan faktor risikonya, atau ketika gejala masih sangat ringan dan belum mengganggu aktivitas sehari-hari.

Referensi : [diabetes.org : diabetes sign and symptoms](https://www.diabetes.org.uk/about-diabetes/symptoms)
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
          Dari bar diagram di atas saya ambil **insight** bahwa ternyata **polyuria dan polydipsia menjadi salah dua gejala yang menandakan pasien positif diabetes.**  
Polyuria (sering buang air kecil) dan polydipsia (haus berlebihan) terjadi karena tubuh mencoba mengeluarkan kelebihan glukosa melalui urin, yang menarik cairan dari jaringan.  
Ini adalah **gejala fisiologis paling awal dan khas pada diabetes,** maka tidak mengherankan jika grafik menunjukkan dominasi keduanya.

Referensi : [clevelandclinic : ketika orang punya sedikit insulin](https://my.clevelandclinic.org/health/diseases/21945-diabetic-ketoacidosis-dka?utm
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
                    
        Gejala-gejala tersebut adalah hasil dari tubuh yang **tidak dapat menggunakan glukosa dengan efektif**, sehingga energi menurun, otot lemas (paresis), dan tubuh merespons dengan makan/minum lebih banyak.  
Ini adalah rantai gejala biologis yang muncul sejak awal diabetes.  

Referensi : [health.grid.id : tanda awal terkena diabetes yang sering diabaikan](https://health.grid.id/read/353596036/inilah-polifagia-tanda-awal-diabetes-tipe-2-yang-sering-terabaikan?page=all)

           
        """)    
        
if __name__ == '__main__':
    eda()