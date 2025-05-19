import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


TRAIN_DATA = [
    # Cuisine
    ("Je cuisine un gâteau", "Cuisine"),
    ("Recette de poulet frit", "Cuisine"),

    # Santé
    ("Je veux dormir", "Santé"),
    ("Je suis très fatigué", "Santé"),
    ("J’ai mal à la tête", "Santé"),
    ("Je dois prendre mes médicaments", "Santé"),

    # Éducation - Cours
    ("J’ai un cours de mathématiques demain", "Éducation - Cours"),
    ("Le professeur a parlé des fonctions", "Éducation - Cours"),

    # Éducation - Examen
    ("Je dois réviser pour l’examen final", "Éducation - Examen"),
    ("L’examen de biologie est bientôt", "Éducation - Examen"),

    # Éducation - Devoir
    ("Je dois finir mon devoir d’histoire", "Éducation - Devoir"),
    ("Le devoir de physique est difficile", "Éducation - Devoir"),

    # Éducation - Projet
    ("Notre projet de science est en retard", "Éducation - Projet"),
    ("On doit rendre le projet lundi", "Éducation - Projet"),

    # Éducation - Conférence
    ("J’assiste à une conférence sur l’IA", "Éducation - Conférence"),
    ("Le conférencier parle de réseaux de neurones", "Éducation - Conférence"),

    # Éducation - Révision
    ("Je relis mes fiches de révision", "Éducation - Révision"),
    ("Il faut que je révise le chapitre 5", "Éducation - Révision"),

    # Loisir
    ("Je vais regarder un film", "Loisir"),
    ("J’écoute de la musique", "Loisir"),

    # Travail
    ("Je dois envoyer un rapport", "Travail"),
    ("Réunion avec l’équipe à 14h", "Travail"),

    # Finance
    ("Je dois payer le loyer", "Finance"),
    ("Vérifie ton compte bancaire", "Finance"),

    # Famille
    ("Je vais chez mes parents", "Famille"),
    ("Appelle ta sœur ce soir", "Famille"),
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