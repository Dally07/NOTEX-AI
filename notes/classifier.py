import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


TRAIN_DATA = [
    ("Je cuisine un gâteau", "Cuisine"),
    ("Recette de poulet frit", "Cuisine"),
    ("Je veux dormir", "Santé"),
    ("Je suis très fatigué", "Santé"),
    ("J’ai un devoir à faire", "Éducation"),
    ("Je dois étudier la biologie", "Éducation"),
]

x = [text for text, label in TRAIN_DATA]
y = [label for text, label in TRAIN_DATA]


# pipeline  NLP
Pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB())
])

# Entrainemant 
Pipeline.fit(x, y)


MODEL_PATH = os.path.join(os.path.dirname(__file__), 'note_classifier.pkl')
joblib.dump(Pipeline, MODEL_PATH)


def load_model():
    return joblib.load(MODEL_PATH)

def predict_category(text):
    model = load_model()
    return model.predict([text])[0]