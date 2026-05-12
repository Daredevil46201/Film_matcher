from data import movies
from core import correct_value

def main():
    print("Добро пожаловать! Вам предлагается выбрать фильм на вечер")
    print("Если фильм нравится - нажмите '1', если не нравиться - нажмите '0'\n")
    
    favorite_1 = set()
    favorite_2 = set()

    print("Очередь пользователя №1:\n")
    for k,v in movies.items():
        print(k)
        choise = correct_value()
        if choise:
            favorite_1.add(k)

    print("Очередь пользователя №2:\n")
    for k,v in movies.items():
        print(k)
        choise = correct_value()
        if choise:
            favorite_2.add(k)

    winners = favorite_1 & favorite_2

    print(f"Выбор пользователя №1: {favorite_1}")
    print(f"Выбор пользователя №2: {favorite_2}")

    if winners:
        print(f"\nФильмы победители на вечер: {winners}")
    else:
        print("\nСовпадений нет. Смотрим Уральские пельмени")
    

if __name__ == "__main__":
    main()