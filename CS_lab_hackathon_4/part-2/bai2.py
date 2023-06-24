laptopsStorage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

user_input_brand_name = input("Input a brand: ")
user_input_amount = int(input("Input amount: "))

laptopsStorage[user_input_brand_name.upper()] = user_input_amount

print("Available products:")
for i in laptopsStorage:
    print(f" - {i}: {laptopsStorage[i]}")