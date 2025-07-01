

  <h1>🧑‍🍳 Recipe Recommendation System (Ingredient-Based)</h1>

  <p>This project is a lightweight and scalable <strong>ingredient-based recipe recommender</strong>. It helps users discover recipes by simply entering the ingredients they have on hand. Built using <code>TF-IDF</code> vectorization and <code>cosine similarity</code>, this system ranks recipes from a curated dataset and displays the top matches.</p>

  <div class="section">
    <h2>🔍 Features</h2>
    <ul>
      <li>Input ingredients in natural language</li>
      <li>Recommends the top 5 closest matching recipes</li>
      <li>Modular, clean codebase (<code>vectorizer.py</code>, <code>app.py</code>)</li>
      <li>Easily extendable with real-world datasets</li>
      <li>Supports both JSON and CSV recipe formats</li>
    </ul>
  </div>

  <div class="section">
    <h2>📂 Project Structure</h2>
    <pre><code>
├── app.py                  # User-facing interface to input ingredients
├── vectorizer.py           # Prepares TF-IDF model and vectorizes recipes
├── recipes.json            # Recipe dataset (auto-saved by vectorizer)
├── vectorizer.pkl          # Saved TF-IDF vectorizer
├── tfidf_matrix.pkl        # TF-IDF matrix for all recipes
└── real_recipes.json       # Your dataset with 100+ recipes
    </code></pre>
  </div>

  <div class="section">
    <h2>🚀 How to Run</h2>
    <ol>
      <li><strong>Clone the Repo</strong>
        <pre><code>git clone https://github.com/your-username/recipe-recommender.git
cd recipe-recommender</code></pre>
      </li>
      <li><strong>Install Dependencies</strong>
        <pre><code>pip install scikit-learn</code></pre>
      </li>
      <li><strong>Generate TF-IDF Model</strong>
        <pre><code>python vectorizer.py</code></pre>
        <p>This reads the dataset, vectorizes the ingredients, and saves the model and matrix.</p>
      </li>
      <li><strong>Run the Recommender</strong>
        <pre><code>python app.py</code></pre>
        <p>Then input ingredients like:</p>
        <pre><code>chicken, garlic, tomato</code></pre>
        <p>You'll see:</p>
        <pre><code>
Top 5 Recipe Matches:

1. Garlic Chicken Stir Fry
   Ingredients: chicken, garlic, soy sauce, onion

2. Tomato Basil Chicken
   Ingredients: chicken, tomato, basil, olive oil
        </code></pre>
      </li>
    </ol>
  </div>

  <div class="section">
    <h2>🧠 Dataset</h2>
    <p>Replace <code>real_recipes.json</code> with your own dataset or extend it.</p>
    <p>Each entry should follow this structure:</p>
    <pre><code>{
  "title": "Garlic Chicken Stir Fry",
  "ingredients": ["chicken", "garlic", "soy sauce", "onion"]
}</code></pre>
  </div>

  <div class="section">
    <h2>📈 Future Improvements</h2>
    <ul>
      <li>Add cooking instructions in output</li>
      <li>Add dietary filters (vegan, keto, etc.)</li>
      <li>Build a web UI using Streamlit or Flask</li>
      <li>Add support for image-based recommendations (Phase 2)</li>
    </ul>
  </div>

  <div class="section">
    <h2>👨‍💻 Authors</h2>
    <p>Designed & implemented by <strong>Your Name</strong><br>
    Contributions: Dataset expansion, model integration, TF-IDF pipeline, interface logic</p>
  </div>

  <div class="section">
    <h2>📄 License</h2>
    <p>MIT License</p>
  </div>

</body>
</html>
