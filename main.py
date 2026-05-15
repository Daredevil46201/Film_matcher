# -*- coding: utf-8 -*-

from data import movies
from core import correct_value
from wheel import spin_wheel

def main():
    print("Добро пожаловать! Вам предлагается выбрать фильм на вечер")
    print("Если фильм нравится - нажмите '1', если не нравиться - нажмите '0' \nДля остановки выбора фильма наберите - 'стоп' \n")
    
    favorite_1 = set()
    favorite_2 = set()

    print("Очередь пользователя №1:\n")
    for k,v in movies.items():
        print(f"Название: {k} \nЖанр: {v["Genre"]} | Год: {v["Year"]} | Рейтинг: {v["Rate"]}\n")
        choise = correct_value()
        if choise:
            favorite_1.add(k)
        elif choise == None:
            break
    print("Фильмы закончились \n")
    
    print("Очередь пользователя №2:\n")
    for k,v in movies.items():
        print(f"Название: {k} \nЖанр: {v["Genre"]} | Год: {v["Year"]} | Рейтинг: {v["Rate"]}\n")
        choise = correct_value()
        if choise:
            favorite_2.add(k)
        elif choise == None:
            break
    print("Фильмы закончились \n")

    winners = favorite_1 & favorite_2

    print(f"Выбор пользователя №1: {favorite_1}")
    print(f"Выбор пользователя №2: {favorite_2}")

    print(spin_wheel(winners))
    
if __name__ == "__main__":
    main()