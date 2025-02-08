import os
import joblib
import pandas as pd
import requests
from flask import Flask, request, render_template, session
from config import TMDB_API_KEY, SECRET_KEY  # Import secure keys

# Flask App Configuration
app = Flask(__name__)
app.secret_key = SECRET_KEY  # Secure secret key

# Load Data
filtered_movie = joblib.load("movie.joblib")  # Preprocessed movie dataset
similarity = joblib.load("similarity.joblib")  # Precomputed similarity matrix

# Get movie list
movie_list = filtered_movie['title_x'].tolist()

def get_movie_poster(movie_title):
    """Fetches the movie poster URL from TMDb API with error handling."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    
    try:
        response = requests.get(url, timeout=5)  # 5-second timeout
        response.raise_for_status()  # Raise error if status code is not 200
        data = response.json()
        
        if data.get("results"):
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for {movie_title}: {e}")

    return "https://via.placeholder.com/200x300?text=No+Image"  # Fallback image

def recommend(movie):
    """Returns recommended movie names and poster URLs separately."""
    try:
        index = filtered_movie[filtered_movie['title_x'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        
        recommended_movies = []
        recommended_posters = []

        for i in distances[1:6]:  # Top 5 recommendations
            title = filtered_movie.iloc[i[0]].title_x
            poster = get_movie_poster(title)
            recommended_movies.append(title)
            recommended_posters.append(poster)
        
        return list(zip(recommended_movies, recommended_posters))
    except IndexError:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    recommended_movies = []
    selected_movie = session.get("selected_movie")  # Retrieve stored selection

    if request.method == "POST":
        selected_movie = request.form.get("movie_name")
        session["selected_movie"] = selected_movie  # Store selection in session
        recommended_movies = recommend(selected_movie)

    return render_template("index.html", movies=movie_list, recommended_movies=recommended_movies, selected_movie=selected_movie)

if __name__ == "__main__":
    app.run(debug=True)
