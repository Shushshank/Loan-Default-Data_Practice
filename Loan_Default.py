import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'voting_classifier_model.pkl'
with open(filename, 'rb') as file:
    voting_clf = pickle.load(file)

# Define a function to predict loan default
def predict_loan_default(input_data):
    prediction = voting_clf.predict([input_data])[0]
    return prediction

# Create a Streamlit app
st.title("Loan Default Prediction App")

# Create input fields for user to enter data
st.header("Enter Loan Applicant Information")
age = st.number_input("Age", min_value=18, max_value=100)
income = st.number_input("Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_history = st.number_input("Credit History (0-1)", min_value=0, max_value=1)
marital_status = st.number_input("Marital Status (0-Divorced, 1-Married, 2-Unmarried)", min_value=0, max_value=2)
loan_purpose = st.number_input("Loan Purpose (0-3)", min_value=0, max_value=3)


# Button to trigger prediction
if st.button("Predict Loan Default"):
    input_data = [age, income, loan_amount, credit_history, marital_status, loan_purpose]
    prediction = predict_loan_default(input_data)
    if prediction == 0:
        st.success("The loan applicant is predicted to not default.")
    else:
        st.error("The loan applicant is predicted to default.")
