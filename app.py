import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download core linguistic dependencies
nltk.download('stopwords')
ps = PorterStemmer()


def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [ps.stem(word) for word in text if not word in stopwords.words('english')]
    return ' '.join(text)


# Load saved artifacts
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

# App styling setup
st.set_page_config(page_title="FraudShield AI", page_icon="🛡️", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #07111f 0%, #10233d 45%, #1f3b5c 100%);
        }
        .hero-card {
            padding: 1.4rem 1.6rem;
            border-radius: 18px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.14);
            backdrop-filter: blur(12px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.22);
            margin-bottom: 1rem;
        }
        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.3rem;
        }
        .hero-subtitle {
            color: #cfe3ff;
            font-size: 1rem;
            line-height: 1.5;
        }
        .info-box {
            padding: 1rem;
            border-radius: 14px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.1);
            color: #eaf4ff;
        }
        div[data-testid="stButton"] > button {
            border-radius: 999px;
            background: linear-gradient(90deg, #2dd4bf 0%, #3b82f6 100%);
            color: white;
            border: none;
            font-weight: 700;
            padding: 0.55rem 1rem;
        }
        div[data-testid="stButton"] > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 8px 20px rgba(59,130,246,0.25);
        }
        textarea {
            border-radius: 14px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">🛡️ FraudShield AI</div>
        <div class="hero-subtitle">A smart assistant for spotting suspicious emails, scam attempts, and phishing-style text in seconds.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("### Paste the message to evaluate")
    user_input = st.text_area("", height=220, placeholder="Example: 'Urgent! Click here to verify your account now...'", label_visibility="collapsed")

    if st.button("🚀 Analyze Message", use_container_width=True):
        if user_input.strip() == "":
            st.warning("Please enter some text to evaluate.")
        else:
            with st.spinner("Scanning linguistic patterns and risk signals..."):
                cleaned = clean_text(user_input)
                vectorized = tfidf.transform([cleaned]).toarray()
                prediction = model.predict(vectorized)[0]

                proba = model.predict_proba(vectorized)[0]
                confidence = proba[prediction] * 100

                st.markdown("### Analysis Result")
                if prediction == 1:
                    st.error("🚨 This message appears suspicious and matches a fraudulent or spam-like pattern.")
                    st.metric(label="Detection Confidence", value=f"{confidence:.2f}%")
                else:
                    st.success("💚 This message looks legitimate and does not show major fraud indicators.")
                    st.metric(label="Detection Confidence", value=f"{confidence:.2f}%")

with col2:
    st.markdown(
        """
        <div class="info-box">
            <b>What this system checks</b><br><br>
            • Urgency and pressure tactics<br>
            • Scam-style wording patterns<br>
            • Suspicious language clusters<br>
            • Likely spam or phishing signals
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("")
    st.info("Tip: Watch for messages that demand immediate action, ask for passwords, or promise unrealistic rewards.")