from data import movies
from core import user_choice
from wheel import spin_wheel

def main():
    print("Добро пожаловать! Вам предлагается выбрать фильм на вечер")
    print("Если фильм нравится - нажмите '1', если не нравиться - нажмите '0' \nДля остановки выбора фильма наберите - 'стоп' \n")
    
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
    
    players_choices = {}
    for i in players:
        players_choices[i] = user_choice(i, movies)

    for k, v in players_choices.items():
        print(f"Выбор пользователя №{k}: {v}")
    
    winners = set.intersection(*players_choices.values())

    if len(winners) == 1:
        print(f"\nФильм победитель на вечер {winners}")
    elif len(winners) > 1:
        print("Добро пожаловать в колесо фортуны \nВыберите режим игры: \nПервый победитель - '1' | Русская рулетка - '0'")
        correct_values = [0, 1]
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
        print(spin_wheel(winners, game_mode))
    else:
        print("\nУвы совпадений нет. Смотрим Уральские пельмени")
    
if __name__ == "__main__":
    main()