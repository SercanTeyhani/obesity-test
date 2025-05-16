# 🩺 Obesity Prediction Project

This project aims to predict obesity levels based on individuals' health metrics and lifestyle behaviors. The workflow includes preprocessing, feature engineering, model building, evaluation, and deployment via a Streamlit web interface.

---

## 🌐 Live Demo

🖥️ Try the application here:  
👉 [https://obesity-test.streamlit.app/](https://obesity-test.streamlit.app/)

Read the full article on Medium:

👉 https://medium.com/@sercanteyhani/predicting-obesity-with-machine-learning-from-raw-data-to-real-time-web-app-5e601f4267e5

---

## 📌 Project Workflow

### **1. Data Preprocessing**
- Verified dataset integrity and confirmed that the data was **balanced** across all obesity categories.
- Handled categorical values using **Label Encoding**.

### **2. Feature Engineering**
- Created a new feature: **BMI (Body Mass Index)** using the formula `BMI = Weight / (Height^2)`, which is a strong indicator of obesity.

### **3. Train-Test Split**
- Split the dataset into **80% training** and **20% testing** subsets using `train_test_split`.

### **4. Feature Scaling**
- Applied **StandardScaler** to normalize input features, improving model performance.

### **5. Model Building: Logistic Regression**
- Trained a **Logistic Regression** model using:
  - `newton-cg` solver
  - `class_weight='balanced'` to handle any potential class imbalance

### **6. Model Evaluation**
- Evaluated the model using:
  - **Classification Report** (precision, recall, F1-score)
  - **Log Loss** for probabilistic accuracy
  - **Confusion Matrix** for class-wise performance

### **7. Model Saving**
- Saved the trained model using **joblib** for later use in the Streamlit app.

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
