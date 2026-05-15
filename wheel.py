import time
from random import choice
from core import correct_value

def spin_wheel(winners):
    if len(winners) == 1:
        return f"\nФильм победитель на вечер {winners}"
    elif len(winners) >= 1:
        print("Добро пожаловать в колесо фортуны \nВыберите режим игры: \nПервый победитель - '1' | Русская рулетка - '0'")
        game = correct_value()
        if game:
            winner = list(winners)
            return f"\nФильм победитель на вечер {choice(winner)}"
        else:
            winner = list(winners)
            while len(winner) > 1:
                print("Крутим барабан")
                drop = choice(winner)
                time.sleep(3)
                print(f"\n{drop} - Выбывает из игры")
                winner.remove(drop)
                print(f"В игре остались: {winner}")
            return f"\nФильм победитель на вечер {choice(winner)}"
    else:
        return "\nУвы совпадений нет. Смотрим Уральские пельмени"    