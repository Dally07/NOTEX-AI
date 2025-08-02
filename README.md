# 🧠 NOTEX_AI - API de Classification Automatique de Notes

**NOTEX_AI** est une API backend développée avec **Django** et **Django REST Framework**, permettant de classifier automatiquement des notes (phrases ou textes) dans une catégorie prédéfinie à l'aide d'un modèle de Machine Learning entraîné localement.

---

## 🚀 Fonctionnalités

- 🔍 **Classification automatique** des textes dans des catégories (Ex : cours, devoir, loisir, etc.).
- 🧠 Classification de texte en **plusieurs intentions** (multi-label)
- 💾 Enregistrement des notes classées dans la base de données.
- 📤 API RESTful pour soumettre un texte et recevoir sa catégorie.
- 🧠 Modèle de classification NLP entraîné avec **scikit-learn**.
- 🔐 Configuration de la base de données via  `.env`.

---

## 🏗️ Stack Technique

- Python 3.x
- Django
- Django REST Framework
- scikit-learn
- joblib (pour la sérialisation du modèle)

---

## 📦 Installation

```bash
git clone https://github.com/Dally07/NOTEX-AI.git
```

```bash
cd NOTEX-AI
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
```
```bash
pip install -r requirements.txt
```

 Lancer le serveur
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
---

🧪 Entraîner le modèle (à faire au premier lancement ou après modification des catégories)

```bash
python manage.py shell
>>> from notes.classifier import train_and_save_model
>>> train_and_save_model()
```
Cela génère un fichier model.joblib contenant le modèle de classification.

---

🔄 API – Classification Multi-Intentions
POST /api/classify/

Analyse une ou plusieurs phrases et retourne leurs intentions détectées.
📥 Requête :

```bash
{
  "phrases": [
    "Je dois faire une révision en biologie",
    "Je vais cuisiner, aller au supermarché, Il faut acheter des œufs au supermarché"
  ]
}
```

📤 Réponse :
```bash
[
  {
    "phrase": "Je dois faire une révision en biologie",
    "categories": ["Éducation - Révision"]
  },
  {
    "phrase": "Je vais cuisiner",
    "categories": ["Cuisine"]
  },
  {
    "phrase": "aller au supermarché",
    "categories": ["Courses"]
  },
  {
    "phrase": "Il faut acheter des œufs au supermarché",
    "categories": ["Courses"]
  }
]
```

🧠 Exemple de données d'entraînement

Le modèle s’entraîne sur un fichier train_data.json contenant des exemples sous la forme :
```bash
[
  {
    "phrase": "Je dois faire une révision en biologie",
    "categories": ["Éducation - Révision"]
  },
  {
    "phrase": "acheter du lait et du pain",
    "categories": ["Courses"]
  }
]
```
---

🔍 Interface Swagger (Documentation de l’API)

Cette API utilise Swagger UI générée automatiquement avec drf-yasg.

    📚 Accéder à la documentation interactive ici :
    👉 http://localhost:8000/swagger/

    📄 Pour la version Redoc :
    👉 http://localhost:8000/redoc/

Ces interfaces permettent :

    de visualiser toutes les routes disponibles,

    de tester les endpoints avec les données d'exemple,

    de comprendre le format d’entrée/sortie de chaque route.

---

✨ À venir

**-Interface frontend (Next.js)**

**-Authentification des utilisateurs**

**-Amélioration du modèle NLP (CamemBERT, transformers…)**

**-Enregistrement par lots (plusieurs phrases)**

**-Export des notes classées**

---

🧑‍💻 Auteur

Dally Maminomenjanahary
📧 dallymaminomenjanahar@gmail.com
🔗 GitHub
📜 Licence
---
Projet open-source sous licence MIT.
