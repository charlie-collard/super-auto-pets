#!/usr/bin/env python3
import json
import re

background = "grass field"

team_1 = [
    ("fish", "lucky", 3, 10, 50, "abandon"),
    ("fish", "lucky", 3, 10, 50, "abandon"),
    ("fish", "lucky", 3, 10, 50, "abandon"),
    ("fish", "lucky", 3, 10, 50, "abandon"),
    ("fish", "lucky", 3, 10, 50, "abandon"),
]

team_2 = [
    ("worm", "lucky", 3, 10, 50, "trophy"),
    ("worm", "lucky", 3, 10, 50, "trophy"),
    ("worm", "lucky", 3, 10, 50, "trophy"),
    ("worm", "lucky", 3, 10, 50, "trophy"),
    ("worm", "lucky", 3, 10, 50, "trophy"),
]

with open("data/abilities.json") as f:
    abilities = json.load(f)

with open("data/animals.json") as f:
    animals = json.load(f)

with open("data/backgrounds.json") as f:
    backgrounds = json.load(f)

with open("data/battle.json") as f:
    data = json.load(f)

with open("data/hats.json") as f:
    hats = json.load(f)

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

def edit_board(team, board_name, board_background, index_function):
    global data
    for i, (animal, perk, level, attack, health, hat) in enumerate(team):
        index = index_function(i)
        animal_id = animals.get(animal)
        if animal_id != None:
            data[board_name]["Minions"]["Items"][index]["Enum"] = animal_id
            data[board_name]["Minions"]["Items"][index]["Abilities"] = [transform_ability(ability_id, level) for ability_id in (abilities.get(animal) or [])]
            data[board_name]["Minions"]["Items"][index]["Level"] = level
            data[board_name]["Minions"]["Items"][index]["Perk"] = perks.get(perk)
            data[board_name]["Minions"]["Items"][index]["Attack"]["Permanent"] = attack
            data[board_name]["Minions"]["Items"][index]["Health"]["Permanent"] = health
            data[board_name]["Minions"]["Items"][index]["Cosmetic"] = hats.get(hat)
        else:
            data[board_name]["Minions"]["Items"][index] = None

    data[board_name]["Background"] = backgrounds.get(board_background)


edit_board(team_1, "UserBoard", background, lambda i: i)
edit_board(team_2, "OpponentBoard", background, lambda i: 4-i)
with open("generated-battle.json", "w") as f:
    json.dump(data, f, indent=2)
