import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TMDb API Key (Store it in .env file securely)
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
