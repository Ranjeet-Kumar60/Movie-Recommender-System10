#!/usr/bin/env python
# coding: utf-8

# # **Movie Recommendation System** 

# ## **Project Overview**
# - This project builds a content-based movie recommendation system using NLP techniques and cosine similarity.  
# - It processes movie metadata, extracts key features, and generates recommendations based on textual similarity.

# ### 1. Import Required Libraries

# In[1]:


import numpy as np
import pandas as pd
import ast  # To parse stringified lists
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib  # For saving the model


# In[2]:


# Display all columns for better visibility
pd.set_option("display.max_columns", None)


# ### 2. Load Datasets
# - 'tmdb_5000_credits.csv' contains movie_id title cast and crew details.
# - 'tmdb_5000_movies.csv' contains metadata like genres, keywords, and overviews etc.

# In[3]:


credits=pd.read_csv("C:/Users/User/OneDrive/Desktop/movie without similarity on github/tmdb_5000_credits.csv")


# In[4]:


movies = pd.read_csv("C:/Users/User/OneDrive/Desktop/movie without similarity on github/tmdb_5000_movies.csv")
movies.head()


# In[5]:


# Display basic information

print(f"Movies Dataset Shape: {movies.shape}")
print(f"Credits Dataset Shape: {credits.shape}")


# 
# ### 3. Merge Datasets on Movie ID

# In[6]:


df_movie=movies.merge(credits,left_on="id",right_on="movie_id")
df_movie.head(1)


# ### 4. Selecting Relevant Features

# In[7]:


# List of columns to drop
columns_to_drop = [
    'budget', 'homepage', 'original_language', 'original_title', 'popularity', 
    'production_companies', 'production_countries', 'release_date', 'revenue', 
    'runtime', 'spoken_languages', 'status', 'tagline', 'vote_average', 'vote_count', 
    'title_y', 'movie_id' 
]

# Droping columns to save memory
selected_movie=df_movie.drop(columns=columns_to_drop)

# Displaying the modified DataFrame
selected_movie.head()


# ### 5. checking duplicated Values

# In[8]:


print("Duplicated Values Before Cleanup:", selected_movie.duplicated().sum())


# ### 5. Checking Missing Values

# In[9]:


print("Missing Values Before Cleanup:\n", selected_movie.isnull().sum())


# In[10]:


selected_movie


# ### 6. Preprocessing Text Data
# - Convert JSON-like string columns into lists of meaningful words.
# 

# In[11]:


def string_from_dict(text):
    return [i['name'].lower().replace(" ", "_") for i in ast.literal_eval(text)]


# In[12]:


# Apply function to genres and keywords
selected_movie['genres']=selected_movie['genres'].apply(string_from_dict)
selected_movie['keywords']=selected_movie['keywords'].apply(string_from_dict)


# In[13]:


# Extract top 3 cast members
def top_cast(text):
    """Extracts the director's name from the crew list."""
    return [i['name'].lower().replace(" ", "_") for index, i in enumerate(ast.literal_eval(text)) if index < 3]

selected_movie['cast'] = selected_movie['cast'].apply(top_cast)


# In[14]:


# Extract director's name
def Director(text):
    """Extracts the director's name from the crew list."""
    return next((i['name'].lower().replace(" ", "_") for i in ast.literal_eval(text) if i['job'] == "Director"), "unknown")

selected_movie['crew'] = selected_movie['crew'].fillna("[]")  # Replace NaN with empty lists in string format to aviod error
selected_movie['crew'] = selected_movie['crew'].apply(Director)  #  To Apply function safely


# In[15]:


selected_movie=selected_movie.dropna(subset=['overview'])


# In[16]:


print(selected_movie.isnull().sum())


# ### 7. Feature Engineering
# - Create a new 'tags' column by combining all relevant textual features.

# In[17]:


selected_movie['tags'] = selected_movie.apply(lambda x: ' '.join(
    [word.replace(" ", "_") for word in (x['genres'] + x['keywords'] + x['cast'] + [x['crew']])] + 
    x['overview'].lower().split()  # Keep words separate
), axis=1)


# In[18]:


selected_movie.head(5)


# In[19]:


selected_movie['tags'][0]


# In[20]:


# Keep only necessary columns for the model
filtered_movie=selected_movie[['id','title_x','tags']].copy()


# In[21]:


filtered_movie.head(5)


# ### 8. Text Vectorization Using CountVectorizer
# - Convert the 'tags' column into a numerical feature vector using Bag-of-Words.

# In[22]:


# Initialize CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

# Convert tags into feature vectors
vectors = cv.fit_transform(filtered_movie['tags']).toarray()


# In[23]:


# Display vocabulary size
print(f"Vectorized Features Shape: {vectors.shape}")


# ### 9. Compute Cosine Similarity
# - Compute similarity scores between movies based on their text features.

# In[24]:


similarity = cosine_similarity(vectors)


# In[25]:


similarity = cosine_similarity(vectors)
print(f"Similarity Matrix Shape: {similarity.shape}")


# ### 10. Build Recommendation Function
# - Function to recommend the top 5 most similar movies based on user input.

# In[26]:


def recommend(movie):

    """Returns top 5 recommended movies based on similarity scores."""
    index = filtered_movie[filtered_movie['title_x'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    print(distances)
    for i in distances:
       return filtered_movie.iloc[i[0]].title_x


# In[27]:


recommend("Avatar")


# ### 12. Save Model for Deployment

# In[28]:


joblib.dump(filtered_movie, "movie.joblib")


# In[ ]:




