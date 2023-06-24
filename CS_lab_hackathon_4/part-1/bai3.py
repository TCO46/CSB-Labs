laptopsStorage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

userInput = input("Input a brand: ")

print(f"Available {userInput}s: {laptopsStorage[userInput.upper()]}")