laptopsStorage = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

def calculate_total_product(dict):
    result = 0
    for i in dict:
        result += dict[i]
    return result

print(f"Total products: {calculate_total_product(laptopsStorage)}")