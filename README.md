Salary Prediction

📌 Introduction
This project focuses on predicting salaries based on multiple professional and demographic factors such as age, gender, education level, job title, and years of experience. A dataset containing 6,704 records and 6 features was used to train and evaluate various machine learning models to identify the most effective approach for accurate salary prediction.

🔧 Data Preprocessing
Handling Missing Values
The dataset was thoroughly checked for null values.

Any rows with missing or inconsistent data were removed to ensure clean and reliable input for modeling.

📊 Data Visualization
Top 10 Highest-Earning Professions

A bar plot showing the top-paying job roles based on average salary.

Distribution of Continuous Variables

A histogram representing the spread of continuous variables such as age and experience.

Distribution of Education Level and Gender

A chart showing how education level and gender are distributed in the dataset.

Correlation Heatmap

A heatmap illustrating the strength of relationships between numerical features.

⚙️ Model Building and Evaluation
Model Selection
Several algorithms were explored and evaluated, including:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

GridSearchCV was used to tune hyperparameters and identify the optimal configuration for each model.

Evaluation Metrics
Models were assessed using the following metrics:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

R² Score

Feature Importance

A bar graph highlighting which features contribute most to predicting salaries.

✅ Results
Random Forest performed best, achieving the highest R² score (0.971) and the lowest error metrics, demonstrating excellent prediction accuracy.

Decision Tree also performed well but with slightly higher error rates.

Linear Regression had the lowest R² score (0.833), showing limitations in modeling complex salary relationships.

📌 Conclusion
The Random Forest Regressor proved to be the most effective model for this salary prediction task.


Author: Vishal Kumar

The analysis revealed that factors such as experience, job title, and education level play a critical role in determining salary.

The project highlights the importance of thorough data preprocessing, careful feature selection, and appropriate model choice in machine learning.

This solution can be applied in HR analytics, recruitment, and compensation planning to generate fair and informed salary insights.

