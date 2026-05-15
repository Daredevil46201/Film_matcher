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

def user_choice(user_id, dict_movies):
    print(f"Очередь пользователя №{user_id}:\n")
    player_favorites = set()
    user_want_to_stop = False
    for k,v in dict_movies.items():
        print(f"Название: {k} \nЖанр: {v["Genre"]} | Год: {v["Year"]} | Рейтинг: {v["Rate"]}\n")
        choise = correct_value()
        if choise == 1:
            player_favorites.add(k)
        elif choise == None:
            user_want_to_stop = True
            break
    if not user_want_to_stop:    
        print("Фильмы закончились \n")
    return player_favorites
