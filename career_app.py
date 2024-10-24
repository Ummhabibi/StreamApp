import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model pipeline
with open('career_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and info for the app
st.title("AI Career Advisor")
st.info("""
    Welcome to the AI Career Advisor! This tool is designed to help you predict suitable career paths based on your personal profile and work experience. 
""")

# Add a brief description and instructions
st.write("""
### Instructions:
1. Select the appropriate options from each dropdown menu that best describe your current situation.
2. If you are transitioning careers, make sure to select 'Yes' in the career transition question.
3. Once all the inputs are selected, click the **Predict** button to see the suggested career path for you.
""")

# Collect user inputs with a default "Please select" option, and set index for default
employment_status = st.selectbox('Employment Status', ['Please select', 'Employed', 'Unemployed'], index=0)
work_experience = st.selectbox('Years of Work Experience', ['Please select', 'Less than 1 year', '1-3', '4-7', '8-10', '10+'], index=0)
age = st.selectbox('Age', ['Please select', '18-24', '25-34', '35-44', '45+'], index=0)
skills = st.selectbox('Skills', ['Please select', 'Finance and Communication', 'Leadership', 'No Skills', 'Problem Solving', 'Tech and Communication', 'Tech and Leadership', 'Time management'], index=0)

# Collect inputs for optional features with default index
personality_type = st.selectbox('Personality Type', ['Please select', 'Introvert', 'Extrovert'], index=0)
work_mode = st.selectbox('Preferred Work Mode', ['Please select', 'Structured', 'Flexible', 'Other'], index=0)
transition_profile = st.selectbox('Transition Profile', ['Please select', 'Financial Balance', 'Fulfilment Priority', 'Other'], index=0)

# Define mappings for categorical inputs (these should match your original encodings)
employment_status_map = {'Employed': 1, 'Unemployed': 0}
personality_type_map = {'Introvert': 1, 'Extrovert': 0}
work_mode_map = {'Other': 0, 'Structured': 1, 'Flexible': 2}
transition_profile_map = {'Other': 0, 'Financial Balance': 1, 'Fulfilment Priority': 2}
work_experience_map = {'Less than 1 year': 0, '1-3': 1, '4-7': 2, '8-10': 3, '10+': 4}
age_map = {'18-24': 0, '25-34': 1, '35-44': 2, '45+': 3}
skills_map = {'Finance and Communication': 0, 'Leadership': 1, 'No Skills': 2, 'Problem Solving': 3, 'Tech and Communication': 4, 'Tech and Leadership': 5, 'Time management': 6}

# Add a check to make sure the user has selected something for all fields
if 'Please select' in [employment_status, work_experience, age, skills, personality_type, work_mode, transition_profile]:
    st.warning("Please select an option for all fields.")
else:
    # Map the user inputs to the numerical values
    employment_status_encoded = employment_status_map[employment_status]
    personality_type_encoded = personality_type_map[personality_type]
    work_mode_encoded = work_mode_map[work_mode]
    transition_profile_encoded = transition_profile_map[transition_profile]
    work_experience_encoded = work_experience_map[work_experience]
    age_encoded = age_map[age]
    skills_encoded = skills_map[skills]

    # Prepare the input data for prediction
    user_data = [[employment_status_encoded, work_experience_encoded, age_encoded, personality_type_encoded, 
                  work_mode_encoded, skills_encoded, transition_profile_encoded]]

    # Define the career path mapping (numeric to career path labels)
    career_path_map = {0: 'Finance or Education', 1: 'Other', 2: 'Science or Engineering', 3: 'Tech'}

    # When the user clicks the "Predict" button
    if st.button('Predict'):
        # Make prediction
        prediction = model.predict(user_data)

        # Convert the numeric prediction to the actual career path
        predicted_career = career_path_map.get(prediction[0], "Unknown career path")

        # Conditional logic based on transition_profile
        if transition_profile == 'Other':
            st.write(f"Consider a career in: {predicted_career}.")
        else:
            st.write(f"A new beginning awaits in: {predicted_career}.")


        
        
        
        
    


