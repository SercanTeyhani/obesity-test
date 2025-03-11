import pandas as pd
import numpy
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

try:
    with open('obesity_logistic_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please make sure the file exists.")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# Title
st.title('Obesity Prediction Application')

# User input fields
age = st.number_input('Enter your age:', min_value=0.0, step=0.01, format="%.2f")
fcvc = st.number_input('Vegetable Consumption Frequency (between 1-3):', min_value=0.0, max_value=3.0, step=0.01, format="%.2f")
ch2o = st.number_input('Daily Water Intake (liters):', min_value=0.0, step=0.01, format="%.2f")
faf = st.number_input('Physical Activity Frequency (hours):', min_value=0.0, step=0.01, format="%.2f")
bmi = st.number_input('Enter your BMI value:', min_value=0.0, step=0.01, format="%.2f")
tue = st.number_input('Regular Exercise Habits (hours):', min_value=0.0, step=0.01, format="%.2f")

# Categorical input fields
gender = st.selectbox('Gender:', ['Male', 'Female'])
family_history = st.selectbox('Family History of Overweight:', ['Yes', 'No'])
favc = st.selectbox('Frequent Consumption of High-Calorie Food (FAVC):', ['Yes', 'No'])
caec = st.selectbox('Consumption of Food Between Meals (CAEC):', ['Frequently', 'Sometimes', 'Never'])
smoke = st.selectbox('Do You Smoke?', ['Yes', 'No'])
scc = st.selectbox('Do You Monitor Your Daily Caloric Intake?', ['Yes', 'No'])
calcs = st.selectbox('Alcohol Consumption (CALC):', ['Frequently', 'Sometimes', 'Never'])
mtrans = st.selectbox('Mode of Transportation:', ['Bicycle', 'Motorbike', 'Public Transport', 'Walking'])
ncp = st.number_input('Eating Habits (between 0-3):', min_value=0.0, max_value=3.0, step=0.01, format="%.2f")

# Add "Test" button
if st.button('Test'):
    try:
        # Create a DataFrame with user input
        input_data = {
            'Gender': [1 if gender == 'Male' else 0],
            'Age': [age],
            'family_history': [1 if family_history == 'Yes' else 0],
            'FAVC': [1 if favc == 'Yes' else 0],
            'FCVC': [fcvc],
            'NCP': [ncp],
            'CAEC': [2 if caec == 'Frequently' else (1 if caec == 'Sometimes' else 0)],
            'SMOKE': [1 if smoke == 'Yes' else 0],
            'CH2O': [ch2o],
            'SCC': [1 if scc == 'Yes' else 0],
            'FAF': [faf],
            'TUE': [tue],
            'CALC': [2 if calcs == 'Frequently' else (1 if calcs == 'Sometimes' else 0)],
            'MTRANS': [0 if mtrans == 'Bicycle' else (1 if mtrans == 'Motorbike' else (2 if mtrans == 'Public Transport' else 3))],
            'BMI': [bmi],
        }

        input_df = pd.DataFrame(input_data)

        # Make a prediction using the model
        prediction = model.predict(input_df)[0]

        # Map prediction results
        result_map = {
            0: 'Underweight',
            1: 'Normal Weight',
            2: 'Obesity Type I',
            3: 'Obesity Type II',
            4: 'Obesity Type III',
            5: 'Overweight Level I',
            6: 'Overweight Level II'
        }

        st.success(f"Result: {result_map.get(prediction, 'Unknown Prediction')}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
