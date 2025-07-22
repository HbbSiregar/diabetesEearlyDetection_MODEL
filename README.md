# Pembuatan Machine Learning untuk mendeteksi diabetes tahap awal

## Repository Outline
1. README.md - Penjelasan tentang project
2. P1M2_ma'ruf_habibie_conceptual.txt -  File txt yang berisi jawaban pertanyaan conceptual
3. P1M2_ma'ruf_habibie.ipynb - Notebook yang berisi proses Pembuatan Machine Learning
4. P1M2_ma'ruf_habbibie_inference.ipynb - Notebook yang berisi inference dari hasil modeling
5. diabetes_data_upload.csv - Dataset yang akan diolah untuk pembuatan Machine Learning
6. description.md - File yang berisi keterangan project
6. deployments/app.py - Script file yang berfungsi sebagai aplikasi untuk deployment model Machine Learning agar    dapat diakses dalam bentuk layanan API atau aplikasi web.
7. deployments/Banner.jpg - Gambar banner untuk file home.py
8. deployments/eda.py - Script file untuk Exploratory Data Analys pada halaman web deployments
9. deployments/home.py -  Script File tampilan awal halaman web deployments
10. deployments/model_Diabetes_Early_Detection.pkl - Hasil Model Machine Learning setelah di hyperparameter tuning
11. deployments/ModelBeforeTuning.pkl - Hasil Model Machine Learning sebelum di hyperparameter tuning
12. deployments/predict.py - File script python untuk halaman pengujian hasil modeling

## Problem Background
Karena begitu banyak makanan manis yang mudah di akses, membuat potensi terkena diabetes jadi tinggi. Maka dari itu diperlukan pengecekan diabetes sedari dini supaya bisa mengatur pola hidup lebih baik dan bisa mencegah resiko yang lebih berat.

## Project Output
Halaman web yang bisa digunakan untuk cek diabetes tahap awal

## Data
Data saya dapatkan dari archive.ics.uci.edu dengan link dibawah ini :
[LINK DATASET](https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset)
Dataset ini terdiri dari 520 baris dan 17 kolom

## Method
Project ini tentang machine learning dimana ditentukan 5 algoritma yang akan kita gunakan yaitu (KNN, SVM, Decison Tree, Random Forest, dan Boost (XGBoost)). Lalu diharuskan juga melakukan hyperparameter tuning.

## Stacks
Bahasa Pemrograman:
- Python (versi minimal yang digunakan bisa dicantumkan)

Library untuk Manipulasi Data & Statistik:
- pandas 
- numpy 
- scipy.stats 
- seaborn & matplotlib.pyplot 

Library untuk Preprocessing dan Pipeline:
- sklearn.preprocessing (StandardScaler, OneHotEncoder, OrdinalEncoder, LabelEncoder)
- sklearn.pipeline (Pipeline, make_pipeline)
- sklearn.compose (ColumnTransformer)
- sklearn.base (BaseEstimator, TransformerMixin untuk custom transformer)
- sklearn.utils.validation (check_is_fitted untuk validasi model dan transformasi)

Library untuk Model Machine Learning:
- sklearn.neighbors (KNeighborsClassifier)
- sklearn.svm (SVC - Support Vector Classifier)
- sklearn.tree (DecisionTreeClassifier)
- sklearn.ensemble (RandomForestClassifier)
- xgboost (XGBClassifier untuk gradient boosting)

Library untuk Model Evaluation & Model Selection:
- sklearn.model_selection (train_test_split, StratifiedKFold, cross_val_score, RandomizedSearchCV, GridSearchCV)
- sklearn.metrics (classification_report, recall_score, confusion_matrix, ConfusionMatrixDisplay)

Utility & Lainnya:
- pickle (untuk penyimpanan dan loading model dalam format serialized)

## References
- https://rohanrangari.medium.com/imbalanced-vs-balanced-dataset-problems-770dcf9352c6
- https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets
- https://kumparan.com/kumparanmom/massa-otot-menyusut-sejak-usia-30-tahun-yuk-perhatikan-ini-moms-23F2kz3V66p  
- https://www.alodokter.com/ketahui-faktor-risiko-diabetes-dan-cara-mengendalikannya
- https://www.alodokter.com/gejala-diabetes-pada-wanita-yang-harus-diwaspadai  
- https://www.alodokter.com/11-gejala-diabetes-pada-kulit-yang-perlu-diketahui  
- https://aido.id/health-articles/obesitas-menjadi-faktor-pemicu-penyakit-diabetes/detail  
- https://www.halodoc.com/artikel/ini-alasan-luka-lebih-susah-sembuh-pada-pengidap-diabetes  
- https://www.halodoc.com/artikel/diabetes-mellitus-dan-gangguan-muskuloskeletal
- LINK DATASET : https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset

---

**Referensi tambahan:**
- https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
- https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
- https://scikit-learn.org/stable/modules/cross_validation.html
- https://www.geeksforgeeks.org/confusion-matrix-machine-learning/

 

