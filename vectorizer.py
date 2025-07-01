# vectorizer.py
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load your real recipe dataset (replace with the full file if needed)
with open("real_recipes.json", "r") as rf:
    recipes = json.load(rf)

# Convert ingredients list to TF-IDF compatible corpus
corpus = [" ".join(recipe["ingredients"]).lower() for recipe in recipes]

# Create TF-IDF vectorizer and fit to the recipe corpus
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Save the vectorizer, matrix, and original recipes
with open("vectorizer.pkl", "wb") as vf:
    pickle.dump(vectorizer, vf)

with open("tfidf_matrix.pkl", "wb") as mf:
    pickle.dump(tfidf_matrix, mf)

with open("recipes.json", "w") as rf:
    json.dump(recipes, rf, indent=4)

print("✅ TF-IDF vectorizer, matrix, and recipes saved successfully.")
