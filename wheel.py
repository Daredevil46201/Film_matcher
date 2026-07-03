import time
from random import choice

def spin_wheel(winners, game_mode):
    winner = list(winners)
    if game_mode:
        return choice(winner)
    else:
        while len(winner) > 1:
            print("Крутим барабан")
            drop = choice(winner)
            time.sleep(3)
            print(f"\n{drop[0]} - Выбывает из игры")
            winner.remove(drop)
            print(f"В игре остались: {winner}")
        return choice(winner)   