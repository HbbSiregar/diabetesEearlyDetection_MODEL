import streamlit as st
import pandas as pd
import pickle

# Load Model Diabetes Early Detection
with open("src/model_Diabetes_Early_Detection.pkl", "rb") as f:
    model = pickle.load(f)


def predict():
    #title
    st.markdown("<h1 style='text-align: center;'>Deteksi Diabetes Tahap Awal</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write(" #### Masukkan Usia, Jenis Kelamin dan Centang Gejala yang kamu rasa alami dalam tubuh kamu")

    with st.form("diabetes_form"):
        Age = st.number_input("Age (Usia pasien)", min_value=0, max_value=120, step=1)
        Gender = st.selectbox("Gender (Jenis kelamin pasien)", options=["Female", "Male"])

        # Manual input untuk setiap gejala
        Polyuria = st.radio("Polyuria (Kondisi sering buang air kecil)", options=["Yes", "No"], index=1, horizontal=True)
        Polydipsia = st.radio("Polydipsia (Rasa haus yang berlebihan)", options=["Yes", "No"], index=1, horizontal=True)
        sudden_weight_loss = st.radio("Sudden weight loss (Penurunan berat badan secara tiba-tiba)", options=["Yes", "No"], index=1, horizontal=True)
        weakness = st.radio("Weakness (Kondisi fisik yang melemah)", options=["Yes", "No"], index=1, horizontal=True)
        Polyphagia = st.radio("Polyphagia (Rasa lapar atau nafsu makan yang berlebihan)", options=["Yes", "No"], index=1, horizontal=True)
        Genital_thrush = st.radio("Genital thrush (Infeksi jamur pada area genital)", options=["Yes", "No"], index=1, horizontal=True)
        Visual_blurring = st.radio("Visual blurring (Penglihatan yang kabur)", options=["Yes", "No"], index=1, horizontal=True)
        Itching = st.radio("Itching (Rasa gatal pada anggota badan)", options=["Yes", "No"], index=1, horizontal=True)
        Irritability = st.radio("Irritability (Mudah marah atau gelisah)", options=["Yes", "No"], index=1, horizontal=True)
        Delayed_healing = st.radio("Delayed healing (Luka yang lama sembuhnya)", options=["Yes", "No"], index=1, horizontal=True)
        Partial_paresis = st.radio("Partial paresis (Kelemahan atau kelumpuhan sebagian otot)", options=["Yes", "No"], index=1, horizontal=True)
        Muscle_stiffness = st.radio("Muscle stiffness (Kekakuan pada otot)", options=["Yes", "No"], index=1, horizontal=True)
        Alopecia = st.radio("Alopecia (Kebotakan atau rambut yang rontok)", options=["Yes", "No"], index=1, horizontal=True)
        Obesity = st.radio("Obesity (Kegemukan)", options=["Yes", "No"], index=1, horizontal=True)

        submitted = st.form_submit_button("Submit")

        dataInf = {
        "age": Age,
        "gender": Gender,
        "polyuria": Polyuria,
        "polydipsia": Polydipsia,
        "sudden_weight_loss": sudden_weight_loss,
        "weakness": weakness,
        "polyphagia": Polyphagia,
        "genital_thrush": Genital_thrush,
        "visual_blurring": Visual_blurring,
        "itching": Itching,
        "irritability": Irritability,
        "delayed_healing": Delayed_healing,
        "partial_paresis": Partial_paresis,
        "muscle_stiffness": Muscle_stiffness,
        "alopecia": Alopecia,
        "obesity": Obesity,
                }

        if submitted :
            df = pd.DataFrame([dataInf])

            # st.write("### Data yang akan diprediksi:")
            # st.dataframe(df)

            prediction = model.predict(df)

            if prediction[0] == 1:
                st.markdown("<h2 style='color: red; text-align: center;'>Positif Diabetes</h2>", unsafe_allow_html=True)
            else:
                st.markdown("<h2 style='color: green; text-align: center;'>Negatif Diabetes</h2>", unsafe_allow_html=True)


if __name__ == '__main__' :
    predict()