import streamlit as st
import joblib
import re

model = joblib.load("NBmodel.pkl")
vectorizer = joblib.load("bOW.pkl")

def clean_text(text):
  text = text.lower()
  text = re.sub(r'[^a-zA-Z\s]', '', text)
  text = re.sub(r'\s+', ' ', text).strip()
  return text


st.title("📱 Spam SMS Detection")

st.write("Enter an SMS below to check whether it is **Spam** or **Ham**.")

sms = st.text_area(
    "Enter your SMS:",
    placeholder="Example: Congratulations! You won a free prize!"
)


if st.button("Predict"):

    if sms.strip() == "":
        st.warning("Please enter an SMS.")

    else:
        # Clean SMS
        clean_sms = clean_text(sms)

        # Convert text to Bag of Words
        sms_bow = vectorizer.transform([clean_sms])

        # Prediction
        prediction = model.predict(sms_bow)[0]

        if prediction == "spam":
            st.error("🚨 SPAM SMS")

        else:
            st.success("✅ HAM — Not Spam")