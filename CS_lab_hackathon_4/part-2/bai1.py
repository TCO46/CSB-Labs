laptopsStorage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

laptopsStorage["TOSHIBA"] = 10

print("Available products:")
for i in laptopsStorage:
    print(f" - {i}: {laptopsStorage[i]}")