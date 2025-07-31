import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load(r"C:\Users\HP CAMO\Downloads\mental_health\mental_health_model.pkl")

st.set_page_config(page_title="Mental Health Checker", page_icon="🧠")
st.title("🧠 Adela Mental Health Checker")
st.markdown("Prediksi kondisi kesehatan mental: Normal, Stres, atau Depresi")

st.divider()

# Input pengguna
sleep_hours = st.slider("Jam tidur rata-rata per hari", 2.0, 12.0, 6.0, step=0.5)
mood_level = st.slider("Level suasana hati (1 = sangat buruk, 10 = sangat baik)", 1, 10, 6)
appetite = st.selectbox("Nafsu makan", ["Menurun", "Normal", "Berlebih"])
concentration = st.slider("Konsentrasi (1 = sangat sulit fokus, 10 = sangat fokus)", 1, 10, 6)
stress_event = st.radio("Apakah sedang mengalami tekanan besar akhir-akhir ini?", ["Ya", "Tidak"])

# Encode input
appetite_map = {"Menurun": 0, "Normal": 1, "Berlebih": 2}
stress_map = {"Tidak": 0, "Ya": 1}
x_input = pd.DataFrame([{
    "sleep_hours": sleep_hours,
    "mood_level": mood_level,
    "appetite_enc": appetite_map[appetite],
    "concentration": concentration,
    "stress_enc": stress_map[stress_event]
}])

# Prediksi
if st.button("🔍 Cek Kondisi Mental"):
    prediction = model.predict(x_input)[0]
    label_map = {0: "Depresi", 1: "Normal", 2: "Stres"}
    label = label_map.get(prediction, "Tidak Diketahui")

    st.subheader(f"Hasil Prediksi: {label}")

    if label == "Normal":
        st.success("✅ Kondisi mental Anda tergolong normal.")
        st.info("Tidur cukup, jaga pola makan dan nikmati hidup dengan seimbang.")
        st.markdown("> 💬 Kamu sudah berada di jalur yang baik. Tetap rawat dirimu dengan cinta dan waktu istirahat yang layak.")

    elif label == "Stres":
        st.warning("⚠️ Tanda-tanda stres terdeteksi.")
        st.info("Cobalah ambil waktu istirahat, atur ulang beban kerja, dan curhat dengan orang terpercaya.")
        st.markdown("> 💬 Tidak apa-apa merasa lelah. Yang penting kamu berani mengakui dan ingin berubah. Itu kekuatan!")

    elif label == "Depresi":
        st.error("🚨 Gejala depresi terdeteksi.")
        st.info("Pertimbangkan bicara dengan psikolog atau psikiater. Jangan ragu untuk meminta bantuan profesional.")
        st.markdown("> 💬 Kamu tidak sendiri. Bahkan dalam gelap, masih ada harapan. Kamu penting dan dicintai.")

st.divider()
st.caption("📌 Aplikasi ini bersifat edukatif dan bukan pengganti diagnosis profesional.")
