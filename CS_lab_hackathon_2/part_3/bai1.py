numbers = [5, 1, 8, 92, -1, 30]

number_input = int(input("Input a number: "))

if number_input in numbers:
    print(f"Number found at position: {numbers.index(number_input) + 1}")
else:
    print("Number not found")
