import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained SVM model, scaler, column names and label encoder

svm_model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")
column_names = joblib.load("model_columns.pkl")
le = joblib.load("label_encoder.pkl")



# Streamlit App

st.set_page_config(
    page_title = "Dry Bean Classification",
    page_icon = "🌱",
    layout = "centered",
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #E8F5E9 0%,
        #C8E6C9 50%,
        #A5D6A7 100%
    );
}
</style>
""", unsafe_allow_html=True)

# Sidebar

st.sidebar.title("About")
st.sidebar.info(
    """
    This application predicts the type of Dry Bean using a trained SVM model.

    Enter all bean measurements and click Predict.
    """
)


st.title("Dry Bean Type Classification")

st.write("Enter the features of the dry bean to predict its type")

# User Inputs
def user_input_features():
    features = {}
    col1, col2, col3 = st.columns(3)

    for i, col in enumerate(column_names):
        if i % 3 == 0:
            with col1:
                features[col] = st.number_input(
                    label = col,
                    value = 0.0,
                    format = "%.4f")
        elif i % 3 == 1:
            with col2:
                features[col] = st.number_input(
                    label = col,
                    value = 0.0,
                    format = "%.4f")
        else:
            with col3:
                features[col] = st.number_input(
                    label = col,
                    value = 0.0,
                    format = "%.4f")
        
    input_data = pd.DataFrame([features])
    return input_data

# User input features
input_df = user_input_features()

# predict Button
if st.button("Predict"):
    # Scale the input data
    input_scaled = scaler.transform(input_df)

    # Predict the class
    prediction = svm_model.predict(input_scaled)
    predicted_class = le.inverse_transform(prediction)[0]

    st.success(f"Predicted Dry Bean Type: {predicted_class}")

