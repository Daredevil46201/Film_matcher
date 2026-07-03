import os
import requests
from datetime import date
from random import randint, shuffle
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


def get_movies(rate, year, no_genre, language, page=1): 
    if not no_genre:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "year": year,
            "with_original_language": language,
            "vote_average.gte": rate,
            "vote_count.gte": 25
        }
    else:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "year": year,
            "with_original_language": language,
            "without_genres": no_genre,
            "vote_average.gte": rate,
            "vote_count.gte": 25
        }

    movie_answer = requests.get(TMDB_URL + "/discover/movie", params = query, proxies = proxies)
    if movie_answer.status_code == 200:
        ma_j=movie_answer.json()
        return ma_j["results"], ma_j.get("total_pages",0)
    else:
        return [], 0

def get_tv(rate, year, no_genre, language, page=1):
    if not no_genre:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "first_air_date.gte": f"{year}-01-01",
            "with_original_language": language,
            "vote_average.gte": rate,
            "vote_count.gte": 25
        }
    else:
        query = {
            "api_key": api_key, 
            "language": LANGUAGE, 
            "page": page,
            "first_air_date.gte": f"{year}-01-01",
            "with_original_language": language,
            "without_genres": no_genre,
            "vote_average.gte": rate,
            "vote_count.gte": 25
        }
    
    tv_answer = requests.get(TMDB_URL + "/discover/tv", params = query, proxies = proxies)
    if tv_answer.status_code == 200:
        tva_j=tv_answer.json()
        return tva_j["results"], tva_j["total_pages"]
    else:
        return [], 0

def get_random_sample(rate, year, no_genre, language, film_tv, current_page=1):
    random_year = randint(year,date.today().year)
    counter_pages = current_page
    
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        if film_tv:
            random_sample, total_pages = get_movies(rate,random_year,no_genre,language,counter_pages)
        else:
            random_sample, total_pages = get_tv(rate,random_year,no_genre,language,counter_pages)
        attempts += 1
        if random_sample:
            break
    if not random_sample:
        return [], counter_pages
    
    if total_pages <= 10:
        counter_pages += 1
        if counter_pages > total_pages:
            counter_pages = 1
    else:
        if total_pages > 50:
            counter_pages = randint(1,50)
        else:
            counter_pages = randint(1,total_pages)
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
    
    if total_pages <= 10:
        return my_list[:10], counter_pages
    else:
        return my_list[:3], counter_pages

def get_random_movie_list(rate, year, no_genre, language, film_tv):
    all_movies = []
    page = 1
    for _ in range(15):
        movies,page = get_random_sample(rate,year,no_genre,language,film_tv,page)
        all_movies.extend(movies)
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

def get_IMDB(TMDB_id):
    URL = "https://www.imdb.com/title/"
    
    query = {
        "api_key": api_key
    }
    
    TMDB_movie = requests.get(TMDB_URL + "/movie/" + TMDB_id + "/external_ids", params = query, proxies = proxies)
    if TMDB_movie.status_code == 200:
        TMDB_movie_j = TMDB_movie.json()
        IMDB_id = TMDB_movie_j["imdb_id"]
        return URL + IMDB_id
    else:
        return None