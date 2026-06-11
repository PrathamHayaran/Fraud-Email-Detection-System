# 🛡️ Fraud & Phishing Email Detection System

An interactive machine learning application built using Natural Language Processing (NLP) to parse, tokenize, clean, and detect fraudulent text patterns in incoming communications.

## 📊 Project Performance Metrics
* **Model Pipeline:** Term Frequency-Inverse Document Frequency (TF-IDF) Vectorizer + Multinomial Naive Bayes Classifier
* **Dataset Scale:** 5,572 distinct text message/email records (UCI Repository)
* **System Evaluation Accuracy:** 98.12%
* **Spam Catching Precision:** 99.00% (High precision rating prevents legitimate emails from showing false alarms)

## 🛠️ Core Technological Stack
* **Language Environment:** Python
* **UI Interface Framework:** Streamlit (Interactive Graphical Layout)
* **Data & Core ML Architecture:** Scikit-Learn, Pandas, NLTK, Regular Expressions (`re`)

## 🚀 Local Deployment Instructions
1. Activate your virtual system module via terminal:
   ```powershell
   .\venv\Scripts\activate


2. Launch the graphical interface engine:
   Bash
   streamlit run app.py
