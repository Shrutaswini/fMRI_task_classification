import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved models
classifier = joblib.load("task_classifier.pkl")
pca = joblib.load("pca_model.pkl")

st.set_page_config(page_title="fMRI Task Classifier", layout="centered")
st.title("🧠 Brain Task Classifier from fMRI Data")

st.markdown("""
Upload a CSV file with fMRI features to classify the cognitive task being performed.
The model uses PCA-reduced BOLD signal features and an SVM classifier.
""")

# Upload input file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Read and transform the data
        data = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data", data.head())

        # Check if input has the same shape (expecting raw features before PCA)
        transformed_data = pca.transform(data)
        prediction = classifier.predict(transformed_data)

        st.success("Prediction complete! 🧠")
        st.write("### Predicted Task Labels:")
        st.write(pd.DataFrame(prediction, columns=["Task"]))

    except Exception as e:
        st.error(f"Error during prediction: {e}")
else:
    st.info("Please upload a CSV file with fMRI features.")
