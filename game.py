import random


def get_weapons() -> str:
    """
    Получение случайного оружия
    :return: str "Лук", "Меч", "Булава"
    """
    weapons = ["Лук", "Меч", "Булава"]
    return random.choice(weapons)


weapon_damage = {
    "Лук": 15,
    "Меч": 20,
    "Булава": 25,  # можно ставить, можно не ставить
}

# print(weapon_damage["Меч"])
# print(random.choice(weapons))

player_one = {
    "name": "Dobruny",
    "hp": 100,
    "weapon": get_weapons(),  # Лук
}

player_two = {
    "name": "Ily",
    "hp": 100,
    "weapon": get_weapons(),
}


def game(player_one: dict, player_two: dict):
    player_one["damage"] = weapon_damage[player_one["weapon"]]
    player_two["damage"] = weapon_damage[player_two["weapon"]]
    print(player_one)
    print(player_two)

    turn = 1

    while True:
        print(f"\n --- Ход {turn}  ---")

        player_two["hp"] -= player_one["damage"]
        print(player_one["name"], "атакует")
        print(player_two["name"], "HP", player_two["hp"])

        if player_two["hp"] <= 0:
            print(f"\n{player_two['name']} проиграл! {player_one} выиграл")
            break

        player_one["hp"] -= player_two["damage"]
        print(player_two["name"], "атакует")
        print(player_one["name"], "HP", player_one["hp"])

        if player_one["hp"] <= 0:
            print(f"\n{player_one['name']} проиграл! {player_two} выиграл")
            break

        turn += 1

    print("Игра закончена")


game(player_one=player_one, player_two=player_two)
