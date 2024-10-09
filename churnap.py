import streamlit as st
import pickle
import pandas as pd

# Load the trained model pipeline
with open('pipeline_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Customer Churn Prediction")

# Collecting user inputs with descriptive labels
customer_tenure = st.number_input("Customer Tenure (Months)", min_value=1.0, value=4.5, step=0.1)
monthly_amount = st.number_input("Monthly Amount Spent ($)", min_value=1.0, value=100.0, step=0.1)
recharge_frequency = st.number_input("Recharge Frequency", min_value=1.0, value=1.0, step=0.1)
revenue_generated = st.number_input("Revenue Generated", min_value=1.0, value=1.0, step=0.1)
frequency_of_use = st.number_input("Frequency of Use", min_value=1.0, value=1.0, step=0.1)
connection_volume = st.number_input("Connection Volume", min_value=1.0, value=1.0, step=0.1)
usage_regularity = st.number_input("Usage Regularity", min_value=1.0, value=1.0, step=0.1)
top_pack_frequency = st.number_input("Top Pack Frequency", min_value=1.0, value=1.0, step=0.1)
total_calls_made = st.number_input("Total Calls Made", min_value=1.0, value=1.0, step=0.1)

# Mapping the inputs to the original feature names expected by the model
features = {
    'TENURE': customer_tenure,
    'MONTANT': monthly_amount,
    'FREQUENCE_RECH': recharge_frequency,
    'REVENUE': revenue_generated,
    'FREQUENCE': frequency_of_use,
    'DATA_VOLUME': connection_volume,
    'REGULARITY': usage_regularity,
    'FREQ_TOP_PACK': top_pack_frequency,
    'TOTAL_CALLS': total_calls_made
}

# Convert the input features to a DataFrame
input_data = pd.DataFrame([features])

# Add a button to make the prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    st.write("Churn Prediction:", "Yes" if prediction[0] == 1 else "No")
