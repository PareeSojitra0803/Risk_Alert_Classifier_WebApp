# 📖 Risk Alert Classifier Documentation


## 🚀 Welcome

The Risk Alert Classifier is a machine learning-powered banking risk assessment system designed to identify customers who may pose a higher financial risk.

This application allows users to explore the dataset, review model performance, analyse visualisations, and predict customer risk interactively.

---

## 🎯 Project Objective

Financial institutions often face challenges in identifying high-risk customers before financial losses occur.

The objective of this project is to develop an early-warning classification system capable of detecting potentially risky customers using historical customer data and machine learning techniques.

---

## 🧠 Machine Learning Pipeline

The project follows a complete supervised learning workflow:

1. Data Cleaning and Preprocessing
2. Missing Value Handling using KNN Imputation
3. Categorical Feature Encoding
4. Class Imbalance Handling using SMOTE
5. Model Training and Evaluation
6. Hyperparameter Tuning
7. Risk Prediction Deployment using Streamlit

---

## 📊 Dataset Information

**Total Records:** 4,600

**Features:** 16

Key customer attributes include:

* Age
* Gender
* Region
* Employment Type
* Annual Income
* Credit Score
* Credit Utilization Ratio
* Missed Payments
* Debt Balance
* Complaints
* Failed Login Attempts
* Account Tenure

---

## 🏆 Final Model

After evaluating multiple classification algorithms, the **Tuned Random Forest Classifier** was selected as the final model.

Reasons:

* Strong Recall Performance
* High F1-Score
* Robust AUC-ROC Performance
* Better Detection of High-Risk Customers

---

## 🤖 Risk Prediction

Navigate to the **Risk Prediction** page using the sidebar.

Enter customer details and click:

**🔍 Predict Customer Risk**

The application will:

* Estimate High-Risk Probability
* Estimate Low-Risk Probability
* Display Risk Assessment
* Generate Prediction Visualisations

---

## 📈 Available Sections

### 🏠 Home

Project overview and key highlights.

### 📊 Dataset Overview

Explore dataset structure and target distribution.

### 📈 Visualizations

Review project charts and model insights.

### 🏆 Model Performance

Compare machine learning models and evaluation metrics.

### 📄 Project Report

Download the detailed theory report.

### 🤖 Risk Prediction

Predict customer risk using the deployed machine learning model.

---

## 💡 Business Impact

This solution can assist financial institutions in:

* Early identification of risky customers
* Improved risk management
* Better decision-making
* Reduced financial losses
* Enhanced customer monitoring

---

## 👩‍💻 Developed By

### *Paree G. Sojitra*

>*Transforming customer data into actionable risk intelligence through Machine Learning.* ⭐
