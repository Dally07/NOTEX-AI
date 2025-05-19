# notes/classifier.py

import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from .traindata import TRAIN_DATA

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'note_classifier.pkl')

def train_and_save_model():
    x = [item["phrase"] for item in TRAIN_DATA]
    y = [item["category"] for item in TRAIN_DATA]

    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('clf', MultinomialNB())
    ])

    pipeline.fit(x, y)
    joblib.dump(pipeline, MODEL_PATH)
    print("✅ Modèle entraîné et sauvegardé avec succès.")

def load_model():
    if not os.path.exists(MODEL_PATH):
        train_and_save_model()
    return joblib.load(MODEL_PATH)

def predict_category(text):
    model = load_model()
    return model.predict([text])[0]
