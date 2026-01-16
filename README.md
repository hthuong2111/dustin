## Obesity Risk Prediction — Machine Learning Project

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="50"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="50"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="50"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/matplotlib/matplotlib-original.svg" width="50"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/seaborn/seaborn-original.svg" width="50"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" width="50"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikit/scikit-original.svg" width="50"/>
</p>

---

### Introduction

This project applies machine learning to analyze how lifestyle habits, genetic predisposition, and daily behaviors influence obesity levels. By identifying key behavioral and physical drivers such as diet, physical activity, and eating patterns, predictive models are built to classify obesity categories. The objective is to provide data-driven insight into the most relevant factors contributing to obesity risk.

---

# Project Questions

- Which lifestyle and behavioral features are most strongly associated with obesity risk?
- Can machine learning models accurately classify obesity levels based on these features?
- Do ensemble methods improve predictive performance compared to baseline models?
- Can obesity risk be estimated using behavioral features alone?

---

# Dataset

**Obesity Levels Dataset (UCI Machine Learning Repository)**

The dataset contains demographic, behavioral, and physical-condition attributes related to eating habits and lifestyle.

- **Target variable:** `NObeyesdad` (7 obesity categories)
- **Features:** Numerical and categorical indicators of daily habits and physical condition

---

# Data Preparation

Initial data preparation and preprocessing were developed in dedicated notebooks and include:

- Data import and inspection  
- Clarification of behavioral indicators (meals, vegetables, water, exercise, screen time)  
- Train/Test split  
- Numerical feature scaling using **StandardScaler**  
- Categorical encoding using **One-Hot Encoding**  
- Preprocessing pipelines using **ColumnTransformer**

A **K-Nearest Neighbors (KNN)** baseline model was implemented as an initial benchmark.

---

# Exploratory Feature Understanding

Feature distributions and correlations were examined to understand behavioral and physical patterns related to obesity. Special attention was given to interpreting behavioral indicators such as:

- Meal frequency (NCP)  
- Vegetable consumption (FCVC)  
- Water intake (CH2O)  
- Physical activity (FAF)  
- Screen time (TUE)

---

# Modeling & Ensemble Learning

Multiple supervised classification models were evaluated across separate notebooks:

- K-Nearest Neighbors (baseline)
- Logistic Regression
- Random Forest
- Gradient Boosting
- Extra Trees (Ensemble)

Cross-validation was applied to assess model stability.  
Hyperparameter tuning using **GridSearchCV** was performed for ensemble models.

Random Forest ensembles consistently outperformed baseline models.

---

# Feature Impact & Ablation Analysis

A dedicated feature impact notebook explored:

- Feature importance ranking  
- Feature ablation experiments  
- Behavioral vs physical feature contribution  

Key findings:

- **Family history of overweight** is a strong genetic risk factor  
- **Eating between meals (snacking)** is a major behavioral risk indicator  
- **Vegetable consumption and physical activity** provide strong protective signals  
- **Public transportation usage** acts as a lifestyle proxy variable  

---

# Behavioral Obesity Risk Model

A final behavioral-risk model was constructed to simulate an **Obesity Risk Calculator**:

- Excludes **Weight, Height, and BMI**
- Uses only behavioral and lifestyle features
- Prioritizes interpretability and real-world usability
- Estimates behavioral similarity to obesity risk patterns

---

# Results

Best-performing ensemble model achieved:

- **Accuracy:** ~98%  
- **Weighted F1-score:** ~0.98  

Cross-validation showed stable performance across folds with low variance.

---

# Conclusions

- Obesity risk is strongly associated with lifestyle behaviors and family history  
- Behavioral variables alone provide meaningful predictive power  
- Ensemble-based models significantly improve performance over baseline classifiers  
- Feature impact analysis enhances interpretability without sacrificing accuracy  
- The behavioral obesity risk calculator provides an interpretable predictive tool  

---

# Next Steps

- Deploy the behavioral risk calculator as a web application  
- Validate models on external real-world datasets  
- Integrate explainability techniques (SHAP)  
- Explore additional ensemble methods (XGBoost, LightGBM)

---

# Team

- Alan Lupatini  
- Christos Vlachakis  
- Hoai Thuong Tran  
- Marta García
  
---

# Key Takeaway

Lifestyle behaviors, dietary patterns, and family history are strong drivers of obesity risk. Machine learning — particularly ensemble-based models — enables accurate prediction and actionable insight into obesity risk factors.
