import sys
from core import user_choice
from wheel import spin_wheel
from api_client import get_genres, get_random_movie_list, get_IMDB
from datetime import date

def ask_year():
    current_year = date.today().year
    
    while True:
        try:
            year = int(input("Введите год отсчёта: "))
            if 1885 <= year <= current_year:
                return year
            else:
                print("Неверный год отсчёта, пожалуйста выберите год в интервале от 1885 до нашего времени")
                continue
        except ValueError:
            print("Неверный тип данных, попробуйте ещё раз")

def ask_rate():
    while True:
        try:
            rate = float(input("Введите рейтинг отсчёта от 0.0 до 10.0: "))
            if 0.0 <= rate <=10.0:
                return rate
            else:
                print("Ваш рейтинг должен находиться в интервале от 0.0 до 10.0, попробуйте ещё раз")
                continue
        except ValueError:
            print("Неверный тип данных, попробуйте ещё раз")

def ask_genres(film_tv):
    genre_list = get_genres(film_tv)
    choose_genres = set()
    print("Вам предлагается выбрать жанры, которые вы не хотите видеть: \nЕсли жанр не нравиться нажмите - '1',  если хотите его оставить - '0'")
    free_choices = (0,1)
    for genre in genre_list:
        while True:
            try:
                user_genre = int(input(f'{genre["name"]}: '))
                if user_genre in free_choices:
                    break
                else:
                    print("Введите '1' или '0'")
                    continue
            except ValueError:
                print("Неверный тип данных, попробуйте ещё раз")
        if user_genre:
            choose_genres.add(genre["id"])
    if choose_genres:
        return choose_genres
    else:
        return set()

def ask_language():
    print("Вам нужно выбрать оригинальные языки стран для фильмов/сериалов \n'Оригинальные языки стран подразумевают под собой - Язык какой страны распространён у снимавших этот фильм/сериал'")
    print("Если страна нравится нажмите - '1', если хотите её убрать нажмите - '0'")
    languages = {"en": "Английский", "ru": "Русский", "ja": "Японский", "ko": "Корейский", "fr":"Французский", "de":"Немецкий", "es":"Испанский", "it":"Итальянский", "zh":"Китайский", "hi":"Индийский", "da":"Датский"}
    free_choices = (0,1)
    user_language = set()
    for k,v in languages.items():
        while True:
            try:
                my_choice = int(input(f'{v}:'))
                if my_choice in free_choices:
                    break
                else:
                    print("Введите '1' или '0'")
                    continue
            except ValueError:
                print("Неверный тип данных, попробуйте ещё раз")
        if my_choice:
            user_language.add(k)
    if user_language:
        return user_language
    else:
        return None
    
def main():
    print("Добро пожаловать! Вам предлагается выбрать фильм/сериал на вечер")
    
    print("\nЧто вы хотите сегодня посмотреть: \nФильмы - 1, Сериалы - 0")
    good_value = (0,1)
    while True:
        try:
            film_tv = int(input())
            if film_tv in good_value:
                break
            else:
                print("Пожалуйста выберите что хотите посмотреть: \nФильмы - 1, Сериалы - 0")
                continue
        except ValueError:
            print("Недопустимое значение. Попробуйте ещё раз")
    
    while True:
        try:
            number_of_players = int(input("Введите количество участников:"))
            if number_of_players > 0:
                break
            else:
                print("Количество игроков должно быть больше нуля")
                continue
        except ValueError:
            print("Недопустимое значение, пожалуйста введите количество участников")

    players = [i for i in range(1, number_of_players + 1)]
    
    player_rate = []
    player_year = []
    no_player_genre = {}
    player_language = {}
    
    for i in players:
        print(f"Очередь пользователя №{i}:")
        player_rate.append(ask_rate())
        player_year.append(ask_year())
        no_player_genre[i] = ask_genres(film_tv)
        player_language[i] = ask_language()
    
    if None in player_language.values():
        print("\nУвы один из вас не хочет смотреть ни одного фильма/сериала на популярном человеческом языке, поэтому мы ничего не сможем найти. Смотрим Уральские пельмени")
        sys.exit()
    
    loosers = set.union(*no_player_genre.values())
    
    if len(loosers) == len(get_genres(film_tv)):
        print("\nУвы один из вас не хочет смотреть ни одного жанра, поэтому мы ничего не сможем найти. Смотрим Уральские пельмени")
        sys.exit()
    
    rate = max(player_rate)
    year = max(player_year)
    no_genre = ",".join(map(str,loosers))
    language = "|".join(set.intersection(*player_language.values()))
    
    if not language:
        print("К сожалению не смогли найти пересечений по выбранным языкам. Смотрим Уральские пельмени")
        sys.exit()
    
    print("Если фильм/сериал нравится - нажмите '1', если не нравится - нажмите '0' \nДля остановки выбора фильма/сериала наберите - 'стоп' \n")
    
    players_choices = {}
    
    print("Загружаем фильмы... Пожалуйста подождите, это может занять некоторое время")
    users_data = get_random_movie_list(rate,year,no_genre,language,film_tv)
    
    if not users_data:
        print("Непредвиденные обстоятельства, мы не смогли найти ни одного фильма/сериала, простите, мы закрываемся")
        sys.exit()
    
    for i in players:
        players_choices[i] = user_choice(i, users_data, film_tv)

    for k, v in players_choices.items():
        title = {title for title, id in v}
        print(f"Выбор пользователя №{k}: {title}")
    
    winners = set.intersection(*players_choices.values())
    print(winners)

    if len(winners) == 1:
        winners, = winners
        print(f"\nПобедитель на вечер - {winners[0]}")
        print("Если желаете, можете перейти на страницу фильма/сериала")
        print(get_IMDB(str(winners[1])))
    elif len(winners) > 1:
        print("Добро пожаловать в колесо фортуны \nВыберите режим игры: \nПервый победитель - '1' | Русская рулетка - '0'")
        correct_values = (0,1)
        while True:
            try:
                game_mode = int(input())
                if game_mode in correct_values:
                    break
                else:
                    print("Ошибка. Допустимые значения: Первый победитель - '1' | Русская рулетка - '0'")
                    continue
            except ValueError:
                print("Ошибка. Допустимые значения: Первый победитель - '1' | Русская рулетка - '0'")
        absolute_winner = spin_wheel(winners, game_mode)
        print(f"\nПобедитель на вечер - {absolute_winner[0]}")
        print("Если желаете, можете перейти на страницу фильма/сериала")
        print(get_IMDB(str(absolute_winner[1])))
    else:
        print("\nУвы совпадений нет. Смотрим Уральские пельмени")

if __name__ == "__main__":
    main()