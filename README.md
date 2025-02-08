# 🎬 Movie Recommendation System  

## 📌 Project Overview  
This project builds a **content-based movie recommendation system** using **Natural Language Processing (NLP)** and **cosine similarity**. It processes movie metadata from **TMDB datasets**, extracts key features, and generates recommendations based on textual similarity.  

### ✨ Key Features:  
✅ Data preprocessing (merging TMDB datasets, handling missing values)  
✅ Feature engineering (creating a unified text representation of each movie)  
✅ NLP techniques (vectorization using CountVectorizer)  
✅ Cosine similarity for recommendation generation  
✅ Flask web app with an interactive UI & movie poster display  
✅ API integration with TMDB for fetching posters  

---  

## 🛠 Technology Stack  
- **Python 3.x**  
- **Pandas, NumPy**  
- **Scikit-learn** (CountVectorizer, Cosine Similarity)  
- **Joblib** (for saving/loading models)  
- **Flask** (web framework)  
- **Requests** (for API calls)  
- **TMDB API** (for movie poster retrieval)  

---  

## 📂 Project Structure  
```
Movie-Recommender-System  
│── static/                   # Stores CSS & JS for Flask  
│   ├── styles.css            # Stylesheet for frontend  
│── templates/                # HTML files for Flask web app  
│   ├── index.html            # Main HTML template  
│── app.py                    # Main Flask application  
│── config.py                 # Configuration settings  
│── movie_recommender_system.ipynb  # Jupyter Notebook for model processing  
│── movie.joblib               # Serialized model file  
│── similarity.joblib          # Similarity matrix for recommendations  
│── README.md                 # Project documentation  
│── requirements.txt          # List of dependencies  
│── tmdb_5000_credits.csv     # TMDB movie credits dataset  
│── tmdb_5000_movies.csv      # TMDB movies dataset   
```  

---  

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash  
git clone https://github.com/Ranjeet-Kumar60/movie_recommender.git  
cd movie_recommender  
```  

### 2️⃣ Install Dependencies  
```bash  
pip install -r requirements.txt  
```  
📌 Example `requirements.txt`:  
```
flask  
joblib  
pandas  
requests  
python-dotenv  
scikit-learn  
```  

### 3️⃣ Set Up Environment Variables  
Create a `.env` file in the root directory and add:  
```ini  
TMDB_API_KEY=your_tmdb_api_key_here  
FLASK_SECRET_KEY=your_secret_key_here  
```  
📌 **Steps to Get TMDB API Key:**  
- Sign up at [The Movie Database (TMDB)](https://www.themoviedb.org/).  
- Navigate to **Account Settings > API** to generate your API key.  

🔑 **Generate a Flask Secret Key:**  
```python  
import secrets  
print(secrets.token_hex(16))  
```  
Copy the generated key and replace `your_secret_key_here` in `.env`.  

🚨 **Never share your `.env` file or hardcode API keys in your code!**  

---  

### 4️⃣ Prepare the Data  
- Ensure `tmdb_5000_credits.csv` and `tmdb_5000_movies.csv` are inside the `data/` folder.  
- Run the Jupyter Notebook to process and save `movie.joblib` & `similarity.joblib`.  

---  

### 5️⃣ Run the Flask Application  
```bash  
python app.py  
```  

### 6️⃣ Access the Application  
Open your browser and visit:  
**http://127.0.0.1:5000/**  

---  

## 🎯 How to Use the Recommendation System  
1. **Select a movie** from the dropdown menu.  
2. Click **"Recommend"** to get **5 movie recommendations** with posters.  

---  

## 📌 Screenshots  
### 🎥 Movie Selection  
![Movie Selection](https://via.placeholder.com/600x300?text=Movie+Selection)  

### 📌 Recommendations  
![Recommendations](https://via.placeholder.com/600x300?text=Recommended+Movies)  

---  

## 🔮 Future Improvements  
🚀 Enhance recommendation with **ratings & user feedback**.  
🚀 Experiment with **TF-IDF** and **deep learning-based embeddings**.  
🚀 Implement **user authentication** for personalized recommendations.  
🚀 Improve **UI/UX with better frontend design**.  

---  

## 🙌 Acknowledgements  
- **TMDB**: For providing movie data & API.  
- **Scikit-learn**: For ML & NLP tools.  
- **Flask**: For the web framework.  
- **Pandas & NumPy**: For data processing.  

---  

## 📜 License  
This project is **free to use** under the MIT License.  

---  

## 🌟 Show Your Support  
⭐ If you like this project, give it a star on GitHub!  
💬 **Have feedback or suggestions?** Feel free to contribute!  

