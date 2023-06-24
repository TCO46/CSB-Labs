laptopsPrice = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

userInput = input("Input a brand: ")

print(f"Price of {userInput}: {laptopsPrice[userInput.upper()]}")