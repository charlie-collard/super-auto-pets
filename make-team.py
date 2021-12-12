import json
import re

team_1 = [
    ("boar", "melon", 3, 50, 50),
    ("boar", "melon", 3, 50, 50),
    ("boar", "melon", 3, 50, 50),
    ("boar", "melon", 3, 50, 50),
    ("snail", "mushroom", 3, 50, 50),
]

team_2 = [
    ("turkey", "melon", 3, 50, 50),
    ("turkey", "melon", 3, 50, 50),
    ("turkey", "melon", 3, 50, 50),
    ("turkey", "melon", 3, 50, 50),
    ("turkey", "melon", 3, 50, 50),
]

with open("data/battle.json") as f:
    data = json.load(f)

with open("data/animals.json") as f:
    animals = json.load(f)

with open("data/abilities.json") as f:
    abilities = json.load(f)

with open("data/perks.json") as f:
    perks = json.load(f)

def transform_ability(ability_id, level):
    return {
        "Enum": ability_id,
        "Level": level,
        "Native": True,
        "Duration": 0,
        "TriggerCount": 1
    }


def edit_board(team, board_name, index_function):
    global data
    for i, (animal, perk, level, attack, health) in enumerate(team):
        index = index_function(i)
        if animal_id := animals.get(animal):
            data[board_name]["Minions"]["Items"][index]["Enum"] = animal_id
            data[board_name]["Minions"]["Items"][index]["Abilities"] = [transform_ability(ability_id, level) for ability_id in (abilities.get(animal) or [])]
            data[board_name]["Minions"]["Items"][index]["Level"] = level
            data[board_name]["Minions"]["Items"][index]["Perk"] = perks.get(perk)
            data[board_name]["Minions"]["Items"][index]["Attack"]["Permanent"] = attack
            data[board_name]["Minions"]["Items"][index]["Health"]["Permanent"] = health
        else:
            data[board_name]["Minions"]["Items"][index] = None


edit_board(team_1, "UserBoard", lambda i: i)
edit_board(team_2, "OpponentBoard", lambda i: 4-i)
with open("generated-battle.json", "w") as f:
    json.dump(data, f, indent=2)
