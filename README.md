# 🩺 Obesity Prediction Project

This project aims to predict obesity levels based on individuals' health metrics and lifestyle behaviors. The workflow includes preprocessing, feature engineering, model building, evaluation, and deployment via a Streamlit web interface.

---

## 🌐 Live Demo

🖥️ Try the application here:  
👉 [https://obesity-test.streamlit.app/](https://obesity-test.streamlit.app/)

🖥️Read the full article on Medium:

👉 https://medium.com/@sercanteyhani/predicting-obesity-with-machine-learning-from-raw-data-to-real-time-web-app-5e601f4267e5

---

## 📌 Project Workflow

# Obesity Prediction Using Machine Learning

---

## 1. Project Overview

This project predicts obesity levels using machine learning, deploying the model as a real-time web application.

---

## 2. Dataset and Preprocessing

- Verified the dataset is balanced across obesity classes.
- Applied Label Encoding to transform categorical variables.
- Split the data into 80% training and 20% testing sets.
- Scaled features using StandardScaler for normalization.

---

## 3. Model Training

- Used Logistic Regression with the `newton-cg` solver.
- Applied `class_weight='balanced'` to handle class imbalance.
- Trained the model on the training dataset.
- Evaluated the model with:
  - Classification report (precision, recall, F1-score)
  - Log Loss metric
  - Confusion matrix for detailed error analysis

---

## 4. Feature Engineering - BMI Creation

- Created a new feature: **BMI (Body Mass Index)** using the formula:  
  **BMI = Weight (kg) ÷ (Height (m))²**
- Incorporated BMI into the dataset to better capture obesity patterns.
- Dropped the original Weight and Height columns to avoid redundancy and multicollinearity.

---

## 5. Feature Importance and Explainability

- Applied SHAP (SHapley Additive exPlanations) to interpret feature impact.
- Visualized feature importance using SHAP summary plots.

---
## 6. Model Retraining

- The model was retrained to improve performance and ensure balanced class handling.

---


### **7. Model Saving**
- Saved the trained model using **joblib** for later use in the Streamlit app.

---


### **8. Streamlit Interface**
- Developed a user-friendly **Streamlit web app** where users can input relevant personal data and receive obesity level predictions in real time.

---

## 🧰 Technologies Used

- **Python**: Data manipulation and modeling  
- **Pandas / NumPy**: Data preprocessing  
- **Matplotlib / Seaborn**: Visualizations  
- **Scikit-learn**: Model building, scaling, evaluation, Confusion matrix & classification metrics, Feature importance analysis  
- **Joblib**: Model persistence  
- **Streamlit**: Web deployment interface
