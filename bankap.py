import streamlit as st
import pickle
import pandas as pd

# Load the trained model pipeline
with open('bank_model.pkl', 'rb') as file:
    model = pickle.load(file)
    st.title("Bank Account Prediction App")

    # Input fields
cellphone_access = st.selectbox("Do you own a cellphone", ["Yes", "No"])
age_of_respondent = st.number_input("Age", min_value=18, max_value=120)
gender_of_respondent = st.selectbox("Gender", ["Male", "Female"])
education_level = st.selectbox("Education Level", ["Tertiary education", "Vocational training", "Secondary education", "Primary education", "Other"])  
job_type = st.selectbox("Do you have an income", ["Yes", "No"])

#Mapping Categorical inputs
education_mapping = {
    'Secondary education': 2, 
    'Vocational training': 3, 
    'Primary education': 1,
    'Tertiary education': 4, 
    'Other': 0}


# Prepare the input data
input_data = {
    'cellphone_access': 1 if cellphone_access == "Yes" else 0,
    'age_of_respondent': age_of_respondent,
    'gender_of_respondent': 1 if gender_of_respondent == "Male" else 0,
    'education_level': education_mapping.get(education_level, -1),
    'job_type': 1 if job_type == "Yes" else 0
}

input_df = pd.DataFrame([input_data])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.success("The user is likely to open a bank account.")
    else:
        st.error("The user is not likely to open a bank account.")
