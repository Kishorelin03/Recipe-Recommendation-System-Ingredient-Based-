

# app.py
import pickle
import json
from sklearn.metrics.pairwise import cosine_similarity

# Load vectorizer, matrix, and recipes
with open("vectorizer.pkl", "rb") as vf:
    vectorizer = pickle.load(vf)

with open("tfidf_matrix.pkl", "rb") as mf:
    tfidf_matrix = pickle.load(mf)

with open("recipes.json", "r") as rf:
    recipes = json.load(rf)

# Get user input
user_input = input("Enter ingredients you have (comma-separated): ")
user_ingredients = " ".join([i.strip().lower() for i in user_input.split(",")])
user_vector = vectorizer.transform([user_ingredients])

# Compute similarity and rank
cosine_similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
top_indices = cosine_similarities.argsort()[::-1][:5]

print("\nTop 5 Recipe Matches:\n")
for idx in top_indices:
    recipe = recipes[idx]
    score = round(float(cosine_similarities[idx]), 4)
    print(f"{recipe['title']} (score: {score})\nIngredients: {', '.join(recipe['ingredients'])}\n")
