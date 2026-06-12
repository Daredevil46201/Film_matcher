import os
import requests
from datetime import date
from dotenv import load_dotenv

today = date.today()

try:
    load_dotenv()
    api_key = os.getenv("API_KEY")
except OSError:
    print("API ключ не найден")

TMDB_URL = "https://api.themoviedb.org/3"
LANGUAGE = "ru-RU"

WINDOWS_HOST_IP = os.getenv("IP_proxie")

proxies = {
    "http": f"http://{WINDOWS_HOST_IP}:10809",
    "https": f"http://{WINDOWS_HOST_IP}:10809"
}

def get_genres(film_tv):
    query = {
        "api_key": api_key
    }
    if film_tv:
        genre_response = requests.get(TMDB_URL + "/genre/movie/list", params = query,proxies = proxies)
    else:
        genre_response = requests.get(TMDB_URL + "/genre/tv/list", params = query, proxies = proxies)
    
    if genre_response.status_code == 200:
        return genre_response.json()["genres"]
    else:
        return []


def get_movies(year, genre_ids): 
    query = {
        "api_key": api_key, 
        "language": LANGUAGE, 
        "page": 1,
        "primary_release_date.gte": f"{year}-01-01",
        "primary_release_date.lte": today,
        "with_genres": genre_ids
    }

    movie_answer = requests.get(TMDB_URL + "/discover/movie", params = query, proxies = proxies)
    print(movie_answer.status_code)
    if movie_answer.status_code == 200:
        print(movie_answer.url)
        ma_j=movie_answer.json()
        return ma_j["results"]
    else:
        return []

def get_tv(year, genre_ids):
    query = {
        "api_key": api_key, 
        "language": LANGUAGE, 
        "page": 1,
        "first_air_date.gte": f"{year}-01-01",
        "first_air_date.lte": today,
        "with_genres": genre_ids
    }
    
    tv_answer = requests.get(TMDB_URL + "/discover/tv", params = query, proxies = proxies)
    print(tv_answer.status_code)
    if tv_answer.status_code == 200:
        print(tv_answer.url)
        tva_j=tv_answer.json()
        return tva_j["results"]
    else:
        return []