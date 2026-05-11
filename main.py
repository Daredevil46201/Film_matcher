movies = ["The Batman", "The Boys", "Pink Panter", "Iron Man", "Social Network", "South Park", "Tron", "La La Land", "The Godfather", "Mortal Kombat"]

favorite_1 = set()
favorite_2 = set()

for i in movies:
    choise = int(input())
    if choise:
        favorite_1.add(i)
print(favorite_1)

for i in movies:
    choise = int(input())
    if choise:
        favorite_2.add(i)
print(favorite_2)

winners = favorite_1 & favorite_2

if winners:
    print(winners)
else:
    print("Совпадений нет. Смотрим Уральские пельмени")