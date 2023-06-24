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


user_input_brand_name = input("Input a brand: ")
user_input_amount = int(input("Input amount to buy: "))

laptopsStorage[user_input_brand_name] -= user_input_amount

print(f"Total price: {laptopsPrice[user_input_brand_name] * user_input_amount}")

print("Available products:")
for i in laptopsStorage:
    print(f" - {i}: {laptopsStorage[i]}")