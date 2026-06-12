import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Risk Alert Classifier",
    page_icon="🚨",
    layout="wide"
)


#Sidebar
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Documentation",
        "Dataset Overview",
        "Visualizations",
        "Model Performance",
        "Project Report",
        "Risk Prediction"
    ]
)

#Home Page
if page == "Home":

    st.title("🚨 Risk Alert Classifier")

    st.markdown("""
    ### A Machine Learning-Based Early Warning System for Identifying High-Risk Banking Customers

    This project predicts whether a banking customer is likely to become a high-risk customer using supervised machine learning techniques, imbalance handling methods, and hyperparameter tuning.
    """)
    
    st.image("images/final_model_comparison.png", use_container_width=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Dataset Size", "4,600")

    with col2:
        st.metric("Features", "16")

    with col3:
        st.metric("Final Model", "Tuned RF")

    st.markdown("---")

    st.subheader("🎯 Business Objective")

    st.write("""
    Financial institutions often struggle to identify risky customers before financial loss occurs.

    The objective of this project is to build an early warning classification system that helps banks proactively identify customers with a higher likelihood of default, fraud, or risky financial behaviour.
    """)

    st.subheader("⚙️ Technologies Used")

    st.write("""
    - Python
    - Pandas
    - NumPy
    - Scikit-Learn
    - Imbalanced-Learn (SMOTE)
    - Matplotlib
    - Streamlit
    """)

#Documentation Page
elif page == "Documentation":
    st.header("📖 Project Documentation")

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())
    except FileNotFoundError:
        st.warning("README.md not found.")


#Dataset Overview Page
elif page == "Dataset Overview":

    st.header("📊 Dataset Overview")

    df = pd.read_csv("data/Risk_Alert_Classifier_Dataset.csv")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Missing Values")

    st.dataframe(df.isnull().sum())

    st.subheader("Target Distribution")

    st.bar_chart(df["risk_status"].value_counts())


#Visualization Page
elif page == "Visualizations":

    st.header("📈 Visualizations")

    st.subheader("Class Imbalance")
    st.image("images/class_imbalance.png")

    st.subheader("Confusion Matrix")
    st.image("images/cm_baseline.png")

    st.subheader("ROC Curves")
    st.image("images/roc_curves.png")

    st.subheader("Feature Importance")
    st.image("images/feature_importance.png")

    st.subheader("Final Model Comparison")
    st.image("images/final_model_comparison.png")
    
    st.subheader("Sampling Technique Comparison")
    st.image("images/sampling_comparison.png")

    st.subheader("Decision Tree vs Random Forest")
    st.image("images/dt_vs_rf_accuracy.png")

    st.subheader("Decision Tree vs Random Forest Confusion Matrices")
    st.image("images/cm_trees.png")


#Model Performance Page
elif page == "Model Performance":

    st.header("🏆 Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Recall", "Best")

    with col2:
        st.metric("F1-Score", "Best")

    with col3:
        st.metric("AUC-ROC", "Best")

    with col4:
        st.metric("Final Model", "RF Tuned")

    st.markdown("---")

    st.subheader("Final Model Comparison")

    st.image("images/final_model_comparison.png")

    st.subheader("Feature Importance")

    st.image("images/feature_importance.png")

    st.success(
        "Tuned Random Forest was selected as the final model because it achieved the strongest balance of Recall, F1-Score and AUC-ROC."
    )
    

#Project Report Page
elif page == "Project Report":

    st.header("📄 Project Report")

    st.info(
        "Detailed project methodology, experimentation, model evaluation, and business interpretation."
    )

    with open("docs/theory_report.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Project Report",
            data=pdf_file,
            file_name="Risk_Alert_Classifier_Report.pdf",
            mime="application/pdf"
        )
        

#Risk Prediction Page
elif page == "Risk Prediction":

    st.header("🤖 Risk Prediction")

    model = joblib.load("risk_model.pkl")

    age = st.number_input("Age", 18, 100, 30)

    gender_text = st.selectbox(
        "Gender",
        ["Female", "Male", "Other"]
    )

    region_text = st.selectbox(
        "Region",
        ["Central", "East", "North", "South", "West"]
    )

    employment_text = st.selectbox(
        "Employment Type",
        ["Salaried", "Unemployed", "Self-Employed", "Retired", "Student"]
    )
    
    gender_map = {
        "Female": 0,
        "Male": 1,
        "Other": 2
    }

    region_map = {
        "Central": 0,
        "East": 1,
        "North": 2,
        "South": 3,
        "West": 4
    }

    employment_map = {
        "Retired": 0,
        "Salaried": 1,
        "Self-Employed": 2,
        "Student": 3,
        "Unemployed": 4
    }

    gender = gender_map[gender_text]
    region = region_map[region_text]
    employment_type = employment_map[employment_text]

    annual_income_inr = st.number_input(
        "Annual Income (INR)",
        value=500000
    )

    credit_score = st.number_input(
        "Credit Score",
        300,
        900,
        650
    )

    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio",
        0.0,
        1.0,
        0.3
    )

    missed_payments_12m = st.number_input(
        "Missed Payments (12 Months)",
        0,
        50,
        0
    )

    avg_late_payment_days = st.number_input(
        "Average Late Payment Days",
        0,
        365,
        0
    )

    monthly_transaction_count = st.number_input(
        "Monthly Transaction Count",
        0,
        1000,
        50
    )

    monthly_spend_inr = st.number_input(
        "Monthly Spend (INR)",
        value=20000
    )

    cash_advance_count_6m = st.number_input(
        "Cash Advance Count (6 Months)",
        0,
        100,
        0
    )

    complaints_last_6m = st.number_input(
        "Complaints (Last 6 Months)",
        0,
        50,
        0
    )

    failed_login_attempts_3m = st.number_input(
        "Failed Login Attempts (3 Months)",
        0,
        100,
        0
    )

    account_tenure_months = st.number_input(
        "Account Tenure (Months)",
        1,
        500,
        24
    )

    debt_balance_inr = st.number_input(
        "Debt Balance (INR)",
        value=10000
    )

    if st.button("Predict Risk"):

        features = np.array([[
            age,
            gender,
            region,
            employment_type,
            annual_income_inr,
            credit_score,
            credit_utilization_ratio,
            missed_payments_12m,
            avg_late_payment_days,
            monthly_transaction_count,
            monthly_spend_inr,
            cash_advance_count_6m,
            complaints_last_6m,
            failed_login_attempts_3m,
            account_tenure_months,
            debt_balance_inr
        ]])

        prediction = model.predict(features)[0]

        probabilities = model.predict_proba(features)[0]

        low_risk_prob = probabilities[0] * 100
        high_risk_prob = probabilities[1] * 100

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "High Risk Probability",
                f"{high_risk_prob:.2f}%"
            )

        with col2:
            st.metric(
                "Low Risk Probability",
                f"{low_risk_prob:.2f}%"
            )
            
        if high_risk_prob >= 70:
            st.warning("Customer requires immediate review.")

        elif high_risk_prob >= 40:
            st.info("Customer should be monitored closely.")

        else:
            st.success("Customer appears financially stable.")

        if prediction == 1:
            st.error("⚠️ High Risk Customer")
        else:
            st.success("✅ Low Risk Customer")