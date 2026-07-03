from api_client import get_poster_url

def correct_value():
    while True:
        value = input("Ваш выбор (1/0/стоп):").lower().strip()
        if value == "0" or value == "1":
            return int(value)
        elif value == "стоп":
            print("Выбор остановлен")
            return None
        else:
            print("Ошибка ввода! \nДопустимыезначения для ввода: Да - '1', Нет - '0', Прекратить выбор - 'стоп' \nПопробуйте ещё раз")
            continue

def user_choice(user_id, dict_movies, film_tv):
    print(f"Очередь пользователя №{user_id}:\n")
    player_favorites = set()
    user_want_to_stop = False
    release = ""
    name = ""
    if film_tv:
        release = "release_date"
        name = "title"
    else:
        release = "first_air_date"
        name = "name"
    for movie in dict_movies:
        print(f"Название: {movie[name]}")
        poster_url = get_poster_url(movie.get("poster_path"))
        if poster_url:
            print(f"Постер: {poster_url}")
        print(f"Описание: {movie["overview"]} | Год: {movie[release][:4]} | Рейтинг: {movie["vote_average"]} | Количество оценок: {movie["vote_count"]}\n")
        choise = correct_value()
        if choise == 1:
            player_favorites.add((movie[name],movie["id"]))
        elif choise == None:
            user_want_to_stop = True
            break
    if not user_want_to_stop:    
        print("Фильмы закончились \n")
    return player_favorites