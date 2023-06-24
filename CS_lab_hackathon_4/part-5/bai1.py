laptopsPrice = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

laptopsStorage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

print("Total value of available brands: ")
for i in laptopsPrice:
    print(f"- {i}: {laptopsPrice[i] * laptopsStorage[i]}")