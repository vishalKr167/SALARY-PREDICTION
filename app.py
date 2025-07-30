import streamlit as st
import pandas as pd
import joblib

# --- Load Artifacts ---
try:
    model = joblib.load('artifacts/model.joblib')
    gender_encoder = joblib.load('artifacts/gender_encoder.joblib')
    model_columns = joblib.load('artifacts/model_columns.joblib')
    job_titles = joblib.load('artifacts/job_titles.joblib')
    education_levels = joblib.load('artifacts/education_levels.joblib')
    education_mapping = joblib.load('artifacts/education_mapping.joblib')
except FileNotFoundError:
    st.error("Model artifacts not found. Please run `train_model.py` first to generate them.")
    st.stop()

# --- Streamlit App UI ---

st.set_page_config(page_title="Salary Prediction", layout="centered")
st.title("💼 Salary Prediction App")
st.write("""
This app predicts the salary of an individual based on their profile.
Please provide the details below to get a salary estimate.
""")

# Create columns for input fields for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=70, value=30, step=1)
    gender = st.selectbox("Gender", options=['Male', 'Female', 'Other'])
    education_level = st.selectbox("Education Level", options=education_levels)

with col2:
    job_title = st.selectbox("Job Title", options=sorted(job_titles))
    years_of_experience = st.number_input("Years of Experience", min_value=0.0, max_value=40.0, value=5.0, step=0.5)

# --- Prediction Logic ---

if st.button("Predict Salary", use_container_width=True, type="primary"):
    # 1. Create a DataFrame from the user's input
    input_data = {
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education_level],
        'Years of Experience': [years_of_experience],
    }
    input_df = pd.DataFrame(input_data)

    # 2. Preprocess the input data (same steps as in training)
    # a. Encode Gender
    input_df['Gender'] = gender_encoder.transform(input_df['Gender'])

    # b. Map Education Level
    input_df['Education Level'] = input_df['Education Level'].map(education_mapping)

    # c. One-Hot Encode Job Title
    # Create a DataFrame with all the model's expected columns, initialized to 0
    processed_df = pd.DataFrame(columns=model_columns, index=input_df.index)
    processed_df.fillna(0, inplace=True)

    # Fill in the values from our input_df
    for col in input_df.columns:
        if col in processed_df.columns:
            processed_df[col] = input_df[col]

    # Set the appropriate job title column to 1
    job_title_col = f"Job Title_{job_title}"
    if job_title_col in processed_df.columns:
        processed_df[job_title_col] = 1

    # Ensure the order of columns is the same as during training
    processed_df = processed_df[model_columns]

    # 3. Make a prediction
    with st.spinner("Predicting..."):
        prediction = model.predict(processed_df)
        predicted_salary = prediction[0]

    # 4. Display the result
    st.success(f"**Predicted Annual Salary: ${predicted_salary:,.2f}**")
    st.balloons()
