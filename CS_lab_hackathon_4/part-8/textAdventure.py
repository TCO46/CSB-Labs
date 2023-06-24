import random

charater = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defend": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread", "Loaf"],
    "Gold": 100,
    "Level": 2
}

skills = {
    1: {
        "Name": "Tackle",
        "Minimum Level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    },

    2: {
        "Name": "Quick Attack",
        "Minimum Level": 2,
        "Damage": 3,
        "Hit rate": 0.5
    },

    3: {
        "Name": "Strong Kick",
        "Minimum Level": 4,
        "Damage": 9,
        "Hit rate": 0.2
    }
}


print(f"Skill 1: {skills[1]['Name']}")
print(f"Skill 2: {skills[2]['Name']}")
print(f"Skill 3: {skills[3]['Name']}")

user_input_skill = int(input("Choose skill by number: "))

print(f"\nYou choose {skills[user_input_skill]['Name']}")

if skills[user_input_skill]["Minimum Level"] > charater["Level"]:
    print(f"Cannot deploy. Required level {skills[user_input_skill]['Minimum Level']}")
elif skills[user_input_skill]["Hit rate"] > random.random():
    print("Missed")
else:
    print(f"Damage: {skills[user_input_skill]['Damage']}")
