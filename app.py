import pandas as pd
import joblib
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Load the model
try:
    model = joblib.load('obesity_logistic_regression_model.pkl')  # Load the .pkl file with joblib
except FileNotFoundError:
    st.error("Model file not found. Please ensure the file exists.")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

# Title
st.title('Obesity Prediction Application')

# Get user input
age = st.number_input('Enter your age:', min_value=0.0, step=0.01, format="%.2f")
fcvc = st.number_input('Frequency of Vegetable Consumption (between 1-3):', min_value=0.0, max_value=3.0, step=0.01, format="%.2f")
ch2o = st.number_input('Daily Water Consumption (liters):', min_value=0.0, step=0.01, format="%.2f")
faf = st.number_input('Physical Activity Frequency (hours):', min_value=0.0, step=0.01, format="%.2f")
bmi = st.number_input('Enter your BMI value:', min_value=0.0, step=0.01, format="%.2f")
tue = st.number_input('Regular Exercise Habit (hours):', min_value=0.0, step=0.01, format="%.2f")

# Dropdowns for categorical variables
gender = st.selectbox('Gender:', ['Male', 'Female'])
family_history = st.selectbox('Is there a family history of obesity?', ['Yes', 'No'])
favc = st.selectbox('High Caloric Food Consumption (FAVC):', ['Yes', 'No'])
caec = st.selectbox('Food Consumption Between Meals (CAEC):', ['Frequently', 'Sometimes', 'Never'])
smoke = st.selectbox('Do you smoke?', ['Yes', 'No'])
scc = st.selectbox('Do you track your daily calorie intake?', ['Yes', 'No'])
calcs = st.selectbox('Alcohol Consumption (CALC):', ['Frequently', 'Sometimes', 'Never'])
mtrans = st.selectbox('Mode of Transportation:', ['Bicycle', 'Motorcycle', 'Public Transport', 'Walking'])
ncp = st.number_input('Consumption Habits (0-3 scale):', min_value=0.0, max_value=3.0, step=0.01, format="%.2f")

# Add "Test" button
if st.button('Test'):
    try:
        # Create a DataFrame from user input
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
            'MTRANS': [0 if mtrans == 'Bicycle' else (1 if mtrans == 'Motorcycle' else (2 if mtrans == 'Public Transport' else 3))],
            'BMI': [bmi],
        }

        input_df = pd.DataFrame(input_data)

        # Make a prediction using the model
        prediction = model.predict(input_df)[0]

        # Map prediction results to labels
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
