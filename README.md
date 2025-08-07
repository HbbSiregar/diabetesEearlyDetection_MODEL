# Early Detection of Diabetes using Machine Learning

## Project Description

This project aims to build an early diabetes detection system using machine learning based on symptom data commonly experienced by patients. With this approach, healthcare workers, families, and individuals can detect the potential for diabetes early on, enabling preventive actions before the condition worsens.

The application is provided as an **interactive web app based on Streamlit**, allowing users to input symptoms and obtain prediction results.

Deployment Link: [https://earlydiabetesdetect.streamlit.app/](https://earlydiabetesdetect.streamlit.app/)

---

## Repository Structure
diabetesEarlyDetection_MODEL/  
├── Deployment/  
│ ├── app.py # Streamlit application entry point  
│ ├── home.py # Initial page display  
│ ├── eda.py # EDA component for interactive page  
│ ├── predict.py # Prediction based on symptom input  
│ ├── model_Diabetes_Early_Detection.pkl # Trained model  
│ ├── diabetes_data_upload.csv # Dataset used  
│ ├── requirements.txt # Dependency list  
│ └── Banner.jpg # Application display banner  
├── diabetes_data_upload.csv # Original dataset  
├── Diabetes_ED.ipynb # Notebook for EDA, preprocessing, modeling  
├── Diabetes_ED_Inference.ipynb # Notebook for trained model implementation  
├── model_Diabetes_Early_Detection.pkl # Final model (backup)  
├── Deployment Link.text # Web app deployment link  
└── README.md # Project documentation  

---

## 🧾 Dataset

Dataset sourced from:  
🔗 [UCI Machine Learning Repository - Early Stage Diabetes Risk Prediction](https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset)  
Data size: 520 rows × 17 columns  
Data types: mixture of categorical and numerical (mostly categorical)  
Target: `class` (`Positive`/`Negative`)

---

## Problem Statement

Excessive sugar consumption has become a common phenomenon triggering a high risk of diabetes. This project develops an early diabetes detection model based on mild clinical symptoms often overlooked, such as excessive thirst, sudden weight loss, and fatigue.

---

## ⚙️ Methods

### Steps:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training with 5 algorithms:
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree
  - Random Forest
  - XGBoost
- Evaluation with cross-validation and recall for the `Positive` class
- Hyperparameter Tuning (GridSearchCV)
- Deployment with Streamlit

### Objective:
Build a classification model with **minimal false negatives**, as misclassifying positive patients as negative can be very dangerous.

---

## Model Evaluation

- Evaluation performed with stratified train-test split (80:20)
- Focus metric: **Recall on positive class**
- Best model saved as `model_Diabetes_Early_Detection.pkl`

---

## Deployment

The application is built using **Streamlit** featuring:
- Data upload
- Visual EDA exploration
- Interactive form for symptom input
- Real-time prediction results

Main file: `Deployment/app.py`

---

## Technologies and Libraries

### Language:
- Python 3.x

### Visualization & Analysis:
- pandas, numpy, seaborn, matplotlib, scipy

### Machine Learning:
- scikit-learn
- xgboost

### Deployment:
- streamlit
- pickle

---

## 🔗 References

### Articles & Medical:
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

### Library & Techniques Documentation:
- https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html  
- https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html  
- https://scikit-learn.org/stable/modules/cross_validation.html  
- https://www.geeksforgeeks.org/confusion-matrix-machine-learning/

---

## Contributors

**Ma’ruf Habibie Siregar**  
GitHub: [github.com/marufhabibie](https://github.com/HbbSiregar)  
