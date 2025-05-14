# obesity-test
🩺 Obesity Prediction Project
This project aims to predict obesity levels based on individuals' health metrics and lifestyle behaviors. The workflow includes preprocessing, feature engineering, model building, evaluation, and deployment via a Streamlit web interface.

📌 Project Workflow
Data Preprocessing

Verified dataset integrity and confirmed that the data was balanced across all obesity categories.

Handled categorical values using Label Encoding.

Feature Engineering

Created a new feature: BMI (Body Mass Index) using the formula BMI = Weight / (Height^2), which is a strong indicator of obesity.

Train-Test Split

Split the dataset into 80% training and 20% testing subsets using train_test_split.

Feature Scaling

Applied StandardScaler to normalize input features, improving model performance.

Model Building: Logistic Regression

Trained a Logistic Regression model using the newton-cg solver and class_weight='balanced' to account for any class imbalances.

Model Evaluation

Evaluated the model using:

Classification Report (precision, recall, F1-score)

Log Loss for probabilistic accuracy

Confusion Matrix for class-wise performance

Model Saving

Saved the trained model using joblib for later use in the Streamlit app.

Streamlit Interface

Developed a user-friendly Streamlit web app where users can input relevant personal data and receive obesity level predictions in real time.

🧰 Technologies Used
Python: Data manipulation and modeling

Pandas / NumPy: Data preprocessing

Matplotlib / Seaborn: Visualizations

Scikit-learn: Model building, scaling, evaluation

Joblib: Model persistence

Streamlit: Web deployment interface
