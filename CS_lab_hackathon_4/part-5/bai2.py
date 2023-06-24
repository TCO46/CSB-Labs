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

result = 0
for i in laptopsPrice:
    result += laptopsPrice[i] * laptopsStorage[i]

print(f"Total value of available items: {result}")
