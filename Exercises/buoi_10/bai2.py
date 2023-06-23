character = {
    "name": "Light",
    "age": 17,
    "strength": 8,
    "defend": 10,
    "HP": 100,
    "backpack": ["shield", "bread", "loaf"],
    "gold": 100,
    "level": 2,
}
character['gold'] += 50
character.update({ "pocket": ["monter dex", "flash light"] })
character['backpack'].append("flint stone")
print(character)