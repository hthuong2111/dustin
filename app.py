import streamlit as st
import pandas as pd
import joblib

st.title("Obesity Risk Calculator")

# Load trained model
model = joblib.load("notebooks/risk_model_pipeline.pkl")


st.write("Enter lifestyle information to estimate obesity risk.")

age = st.number_input("Age", 10, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
family_history = st.selectbox("Family history of overweight?", ["yes", "no"])
favc = st.selectbox("High-calorie food frequently?", ["yes", "no"])
fcvc = st.slider("Vegetable consumption (1–3)", 1.0, 3.0, 2.0)
ncp = st.slider("Meals per day", 1.0, 4.0, 3.0)
caec = st.selectbox("Snacks between meals", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Do you smoke?", ["yes", "no"])
ch2o = st.slider("Water intake (liters/day)", 1.0, 3.0, 2.0)
scc = st.selectbox("Monitor calories?", ["yes", "no"])
faf = st.slider("Physical activity (days/week)", 0.0, 3.0, 1.0)
tue = st.slider("Screen time (0–2)", 0.0, 2.0, 1.0)
calc = st.selectbox("Alcohol consumption", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox(
    "Transportation",
    ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"]
)

if st.button("Calculate Risk"):
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }])

    probs = model.predict_proba(input_df)[0]

    st.subheader("Risk probabilities")
    st.write(f"Low risk: {probs[0]:.1%}")
    st.write(f"Medium risk: {probs[1]:.1%}")
    st.write(f"High risk: {probs[2]:.1%}")

