import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import streamlit as st

@st.cache_resource
def load_model():
    data = pd.read_csv("data/internships.csv")

    X = data["description"]
    y = data["label"]

    vectorizer = TfidfVectorizer(stop_words="english")
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vec, y)

    return model, vectorizer

model, vectorizer = load_model()

def predict_risk(text):
    text_vec = vectorizer.transform([text])
    prob = model.predict_proba(text_vec)[0][1]
    return int(prob * 100)
