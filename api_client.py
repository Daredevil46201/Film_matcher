import os
import requests
from datetime import date
from random import randint, uniform, shuffle
from dotenv import load_dotenv

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


def get_movies(rate, year, no_genre, page=1): 
    if not no_genre:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "year": year,
            "vote_average.gte": rate
        }
    else:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "year": year,
            "without_genres": no_genre,
            "vote_average.gte": rate
        }

    movie_answer = requests.get(TMDB_URL + "/discover/movie", params = query, proxies = proxies)
    if movie_answer.status_code == 200:
        ma_j=movie_answer.json()
        return ma_j["results"]
    else:
        return []

def get_tv(rate, year, no_genre, page=1):
    if not no_genre:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "first_air_date.gte": f"{year}-01-01",
            "vote_average.gte": rate
        }
    else:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "first_air_date.gte": f"{year}-01-01",
            "without_genres": no_genre,
            "vote_average.gte": rate
        }
    
    tv_answer = requests.get(TMDB_URL + "/discover/tv", params = query, proxies = proxies)
    if tv_answer.status_code == 200:
        tva_j=tv_answer.json()
        return tva_j["results"]
    else:
        return []

def get_random_sample(rate, year, no_genre, film_tv):
    random_year = randint(year,date.today().year)
    random_rate = uniform(rate,10.0)
    random_page = randint(1,16)
    
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:
        if film_tv:
            random_sample = get_movies(random_rate,random_year,no_genre,random_page)
        else:
            random_sample = get_tv(random_rate,random_year,no_genre,random_page)
        attempts += 1
        if random_sample:
            break
    if not random_sample:
        return []
    
    my_list = []
    release = ""
    if film_tv:
        release = "release_date"
    else:
        release = "first_air_date"
    for i in random_sample:
        if i["overview"] and year <= int(i[release][:4]) <= date.today().year:
            my_list.append(i)
    shuffle(my_list)
    return my_list[:3]

def get_random_movie_list(rate, year, no_genre, film_tv):
    all_movies = []
    for i in range(15):
        i = get_random_sample(rate,year,no_genre,film_tv)
        all_movies.extend(i)
    unique_movies = {}
    for movies in all_movies:
        unique_movies[movies["id"]] = movies
    result = list(unique_movies.values())
    shuffle(result)
    return result

def get_poster_url(poster_path):
    URL = "https://image.tmdb.org/t/p/w500"
    if poster_path:
        return URL + poster_path
    else:
        return None