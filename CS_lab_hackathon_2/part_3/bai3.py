numbers = []

print("Input the list of numbers.\nEnter 0 to finish.")

while 0 not in numbers:
    input_number = int(input())
    numbers.append(input_number)

print(sum(numbers))
