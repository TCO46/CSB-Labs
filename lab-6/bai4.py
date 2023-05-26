items = int(input("Number of items: "))

prices = []

menu = []

for i in range(items):
    i+=1
    item = input(f"Item {i}: ")
    price = float(input(f"Price of item {i}: "))
    prices.append(price)
    item_and_price = (item, price)
    
    menu.append(item_and_price)

average_price = sum(prices) / items
print(f"Average price: {average_price}")

for i in range(len(prices)):
    if prices[i] > average_price:
        print(menu[i])