laptopsPrice = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}

user_input_brand_name = input("Input a brand: ")
user_input_amount = int(input("Input amount to buy: "))

print(f"Total price: {laptopsPrice[user_input_brand_name] * user_input_amount}")