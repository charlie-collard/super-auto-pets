import json
import re

team_1 = [
    ("none", "none", 3, 50, 50),
    ("none", "none", 3, 50, 50),
    ("none", "none", 3, 50, 50),
    ("tiger", "none", 3, 1, 1),
    ("octopus", "cherry", 3, 1, 1),
]

team_2 = [
    ("deer", "none", 2, 50, 15),
    ("deer", "none", 2, 50, 15),
    ("whale", "none", 2, 50, 15),
    ("rooster", "none", 3, 50, 15),
    ("rooster", "none", 3, 50, 15),
]

with open("battle.json") as f:
    data = json.load(f)

with open("animals") as f:
    animals = f.read().split("\n")

with open("abilities") as f:
    abilities = f.read().split("\n")

with open("perks") as f:
    perks = f.read().split("\n")

def animal_id(animal):
    try:
        return next(a for a in animals if animal.lower() in a.lower()).split(" ")[0]
    except StopIteration:
        return None

def ability_id(animal):
    return next(a for a in abilities if re.search(f"\\b{animal.lower()}\\b", a.lower())).split(" ")[0]

def perk_id(perk):
    try:
        return next(p for p in perks if perk.lower() in p.lower()).split(" ")[0]
    except StopIteration:
        return None


for i, (animal, perk, level, attack, health) in enumerate(team_1):
    if animal_id(animal):
        data["UserBoard"]["Minions"]["Items"][i]["Enum"] = animal_id(animal)
        data["UserBoard"]["Minions"]["Items"][i]["Abilities"][0]["Enum"] = ability_id(animal)
        data["UserBoard"]["Minions"]["Items"][i]["Abilities"][0]["Level"] = level
        data["UserBoard"]["Minions"]["Items"][i]["Level"] = level
        data["UserBoard"]["Minions"]["Items"][i]["Perk"] = perk_id(perk)
        data["UserBoard"]["Minions"]["Items"][i]["Attack"]["Permanent"] = attack
        data["UserBoard"]["Minions"]["Items"][i]["Health"]["Permanent"] = health
    else:
        data["UserBoard"]["Minions"]["Items"][i] = None


for i, (animal, perk, level, attack, health) in enumerate(team_2):
    if animal_id(animal):
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Enum"] = animal_id(animal)
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Abilities"][0]["Enum"] = ability_id(animal)
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Abilities"][0]["Level"] = level
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Level"] = level
        data["OpponentBoard"]["Minions"]["Items"][4-i]["Perk"] = perk_id(perk)
        data["OpponentBoard"]["Minions"]["Items"][i]["Attack"]["Permanent"] = attack
        data["OpponentBoard"]["Minions"]["Items"][i]["Health"]["Permanent"] = health
    else:
        data["OpponentBoard"]["Minions"]["Items"][4-i] = None

with open("generated-battle.json", "w") as f:
    json.dump(data, f, indent=2)