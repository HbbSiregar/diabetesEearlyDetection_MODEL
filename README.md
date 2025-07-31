# Early Detection of Diabetes using Machine Learning

## Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem deteksi dini diabetes menggunakan machine learning berbasis data gejala yang sering dialami oleh pasien. Dengan pendekatan ini, tenaga medis, keluarga, maupun individu dapat mendeteksi potensi diabetes sejak awal, sehingga bisa mengambil tindakan preventif sebelum kondisinya berkembang menjadi lebih serius.

Aplikasi ini disediakan dalam bentuk **web app interaktif berbasis Streamlit** yang memungkinkan pengguna mengisi gejala dan memperoleh hasil prediksi.

Link Deployment: [https://earlydiabetesdetect.streamlit.app/](https://earlydiabetesdetect.streamlit.app/)

---

## Struktur Repository
diabetesEarlyDetection_MODEL/  
├── Deployment/  
│ ├── app.py # Entry point aplikasi Streamlit  
│ ├── home.py # Tampilan awal halaman  
│ ├── eda.py # Komponen EDA untuk halaman interaktif  
│ ├── predict.py # Prediksi berbasis input gejala  
│ ├── model_Diabetes_Early_Detection.pkl # Model terlatih  
│ ├── diabetes_data_upload.csv # Dataset yang digunakan  
│ ├── requirements.txt # Daftar dependensi  
│ └── Banner.jpg # Banner tampilan aplikasi  
├── diabetes_data_upload.csv # Dataset asli  
├── Diabetes_ED.ipynb # Notebook proses EDA, preprocessing, modeling  
├── Diabetes_ED_Inference.ipynb # Notebook untuk implementasi model terlatih  
├── model_Diabetes_Early_Detection.pkl # Model final (backup)  
├── Deployment Link.text # Link deployment web app  
└── README.md # Dokumentasi proyek ini  

---

## 🧾 Dataset

Dataset diperoleh dari:  
🔗 [UCI Machine Learning Repository - Early Stage Diabetes Risk Prediction](https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset)  
Jumlah data: 520 baris × 17 kolom  
Tipe data: campuran antara kategorikal dan numerikal (mayoritas kategorikal)  
Target: `class` (`Positive`/`Negative`)

---

## Permasalahan

Konsumsi gula berlebih telah menjadi fenomena umum dan memicu risiko diabetes yang tinggi. Proyek ini mengembangkan model deteksi dini diabetes berdasarkan gejala-gejala klinis ringan yang sering diabaikan, seperti haus berlebih, penurunan berat badan mendadak, dan kelelahan.

---

## ⚙️ Metode

### Tahapan:
- Exploratory Data Analysis (EDA)
- Feature Engineering 
- Model Training dengan 5 algoritma:
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree
  - Random Forest
  - XGBoost
- Evaluasi dengan cross-validation dan recall pada kelas `Positive`
- Hyperparameter Tuning (GridSearchCV)
- Deployment dengan Streamlit

### Tujuan:
Membangun model klasifikasi yang **minim false negative**, karena kesalahan mendeteksi pasien positif sebagai negatif bisa sangat berbahaya.

---

## Evaluasi Model

- Evaluasi dilakukan dengan stratified train-test split (80:20)
- Fokus metrik: **Recall pada kelas positif**
- Model terbaik disimpan sebagai `model_Diabetes_Early_Detection.pkl`

---

## Deployment

Aplikasi dibangun menggunakan **Streamlit** dengan fitur:
- Upload data
- Eksplorasi EDA visual
- Form interaktif untuk input gejala
- Hasil prediksi ditampilkan secara real-time

File utama: `Deployment/app.py`

---

## Teknologi dan Library

### Bahasa:
- Python 3.x

### Visualisasi & Analisis:
- pandas, numpy, seaborn, matplotlib, scipy

### Machine Learning:
- scikit-learn
- xgboost

### Deployment:
- streamlit
- pickle

---

## 🔗 Referensi

### Artikel & Medis:
- https://rohanrangari.medium.com/imbalanced-vs-balanced-dataset-problems-770dcf9352c6  
- https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets  
- https://kumparan.com/kumparanmom/massa-otot-menyusut-sejak-usia-30-tahun-yuk-perhatikan-ini-moms-23F2kz3V66p  
- https://www.alodokter.com/ketahui-faktor-risiko-diabetes-dan-cara-mengendalikannya  
- https://www.alodokter.com/gejala-diabetes-pada-wanita-yang-harus-diwapadai  
- https://www.alodokter.com/11-gejala-diabetes-pada-kulit-yang-perlu-diketahui  
- https://aido.id/health-articles/obesitas-menjadi-faktor-pemicu-penyakit-diabetes/detail  
- https://www.halodoc.com/artikel/ini-alasan-luka-lebih-susah-sembuh-pada-pengidap-diabetes  
- https://www.halodoc.com/artikel/diabetes-mellitus-dan-gangguan-muskuloskeletal  

### Dataset:
- [UCI Repository - Early Stage Diabetes Risk Prediction Dataset](https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset)

### Dokumentasi Library & Teknik:
- https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html  
- https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html  
- https://scikit-learn.org/stable/modules/cross_validation.html  
- https://www.geeksforgeeks.org/confusion-matrix-machine-learning/

---

## Kontributor

**Ma’ruf Habibie Siregar**  
GitHub: [github.com/marufhabibie](https://github.com/HbbSiregar)  