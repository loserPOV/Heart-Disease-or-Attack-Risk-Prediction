>**Objectives**: Developed a machine learning project utilizing several model algorithms such as SVM,
KNN, Decision Tree, Random Forest, and XGBoost to predict whether someone has a risk of contracting a
Heart Disease or Attack, using dataset from BRFSS 2015 Codebook Report which includes several data such
as BMI, Age, and Medical History(Stroke, Diabetes, etc).

>**Technology / Tools**: Python, Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn, Imblearn, Feature-Engine,
Streamlit, HuggingFace.

>**Dataset**: heart_disease_health_indicators_BRFSS2015.csv

>**Results**:

#### EDA Conclusion:

From the provided data on heart disease, smoking status, age, gender, and Body Mass Index (BMI), the following conclusions can be drawn:

1. **Smoking and Heart Disease:**
   - The data on smoking show that individuals who smoke (Smoker=1) tend to have a higher number of heart disease cases compared to non-smokers (Smoker=0).

2. **Age and Heart Disease:**
   - Age group analysis indicates that the risk of heart disease tends to increase with age. Older age groups have a higher number of heart disease cases.

3. **Gender and Heart Disease:**
   - From the gender data, a direct conclusion cannot be drawn, but it is important to note that the distribution of heart disease cases may vary between men (Sex=1) and women (Sex=0).

4. **BMI and Heart Disease:**
   - It appears that individuals with higher BMI values tend to have a higher number of heart disease cases. There is a positive correlation between BMI values and the risk of heart disease.

5. **General Conclusion:**
   - In general, factors such as smoking, age, gender, and BMI can influence the risk of heart disease.
   - Further analysis, such as statistical tests, may be required to confirm these links in more detail and comprehensively.

   These conclusions are general and based on visual observations of the provided data. For a deeper understanding and statistical validity, further analysis and the application of appropriate statistical methods are required.

#### Model Conclusion:

1. **Metric Focus**
   - The primary focus is to minimize the prediction of someone with heart disease as not having heart disease (minimizing false negatives), preferably focusing on the Recall metric.
   Recall is the ratio of correct positive predictions to all actual positives. In the context of heart disease prediction models, maximizing recall means minimizing the number of actual heart disease cases wrongly classified as non-cases.

2. **Cross Validation**
   - The cross-validated XGBoost model achieved an average recall of about 0.815 with a small standard deviation, indicating consistent performance across different folds. The recall on the test set also falls within a relatively narrow range, indicating model performance stability. The best model is identified as "XGBoost."

3. **Hyperparameter Tuning**
    1. **Best Parameters:**
        - 'xg__gamma': 5
        - 'xg__learning_rate': 0.2
        - 'xg__max_depth': 5
        - 'xg__min_child_weight': 1
        - 'xg__scale_pos_weight': 5
        - 'xg__subsample': 1

    2. **Best Cross Validation Score:**
        - Best Score: 0.953

    - These results indicate that the above parameter combination achieved the highest cross-validation score, approximately 95.4%. This score reflects the model's performance on the training data during grid search.

    - These best parameters can be useful for configuring the XGBoost model to achieve optimal performance based on the specific dataset and problem. The high Cross Validation score indicates that the selected parameters are effective for the task.

4. **Model Evaluation**
    - Looking at the Recall score, this model can very well predict False Negatives with a Recall of 0.95 (train) and 0.96 (test).

    - However, values for other metrics can be considered quite poor, for example, the precision value on the test (0.11). This means that the model tends to predict all data as 1 or having heart disease.

    - The recommendation is to seek better data with more specific features so the model can more easily predict each class or to find a dataset with a more balanced percentage of each class. Further model and Hyperparameter search can also be done to find the most suitable model for making predictions on this data, for example, trying a Logistic Regression model.

>**Deployment**: you can try the deployed model on -> https://huggingface.co/spaces/LoserPOV/Heart_Disease_Prediction