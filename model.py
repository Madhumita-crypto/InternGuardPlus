import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st

@st.cache_resource
def load_model():
    BASE_DIR = os.getcwd()
    DATA_PATH = os.path.join(BASE_DIR, "data", "internships.csv")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

    data = pd.read_csv(DATA_PATH)

    X = data["description"]
    y = data["label"]

    vectorizer = TfidfVectorizer(stop_words="english")
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vec, y)

    return model, vectorizer

model, vectorizer = load_model()

def predict_risk(text):
    vec = vectorizer.transform([text])
    prob = model.predict_proba(vec)[0][1]
    return int(prob * 100)
