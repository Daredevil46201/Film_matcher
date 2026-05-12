movies = ["The Batman", "Iron Man", "Social Network", "South Park", "La La Land"]

favorite_1 = set()
favorite_2 = set()

def correct_value():
    while True:
        value = input().strip()
        if value == "0" or value == "1":
            return int(value)
        else:
            print("Ошибка ввода! \nДопустимыезначения для ввода: Да - '1', Нет - '0' \nПопробуйте ещё раз")
    

print("Добро пожаловать! Вам предлагается выбрать фильм на вечер")
print("Если фильм нравится - нажмите '1', если не нравиться - нажмите '0'\n")

print("Очередь пользователя №1:\n")
for i in movies:
    print(i)
    choise = correct_value()
    if choise:
        favorite_1.add(i)

print("Очередь пользователя №2:\n")
for i in movies:
    print(i)
    choise = correct_value()
    if choise:
        favorite_2.add(i)

winners = favorite_1 & favorite_2

print(f"Выбор пользователя №1: {favorite_1}")
print(f"Выбор пользователя №2: {favorite_2}")

if winners:
    print(f"\nФильмы победители на вечер: {winners}")
else:
    print("\nСовпадений нет. Смотрим Уральские пельмени")