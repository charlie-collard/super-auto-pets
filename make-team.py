import json
import re

team_1 = [
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
]

team_2 = [
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
    ("whale", "melon", 3, 50, 50),
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

for i, (animal, perk, level, attack, health) in enumerate(team_1):
    if animal_id := animals.get(animal):
        data["UserBoard"]["Minions"]["Items"][i]["Enum"] = animal_id
        data["UserBoard"]["Minions"]["Items"][i]["Abilities"] = [transform_ability(ability_id, level) for ability_id in (abilities.get(animal) or [])]
        data["UserBoard"]["Minions"]["Items"][i]["Level"] = level
        data["UserBoard"]["Minions"]["Items"][i]["Perk"] = perks.get(perk)
        data["UserBoard"]["Minions"]["Items"][i]["Attack"]["Permanent"] = attack
        data["UserBoard"]["Minions"]["Items"][i]["Health"]["Permanent"] = health
    else:
        data["UserBoard"]["Minions"]["Items"][i] = None


for i, (animal, perk, level, attack, health) in enumerate(team_2):
    if animal_id := animals.get(animal):
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Enum"] = animal_id
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Abilities"] = [transform_ability(ability_id, level) for ability_id in abilities[animal]]
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Level"] = level
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Perk"] = perks.get(perk)
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Attack"]["Permanent"] = attack
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Health"]["Permanent"] = health
    else:
        data["OpponentBoard"]["Minions"]["Items"][4-i] = None

with open("generated-battle.json", "w") as f:
    json.dump(data, f, indent=2)
