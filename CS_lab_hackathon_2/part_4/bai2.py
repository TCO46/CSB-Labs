numbers = []
even_numbers = []

print("Input the list of numbers.\nEnter 0 to finish.")

while 0 not in numbers:
    input_number = int(input())
    numbers.append(input_number)

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

even_numbers.remove(0)
print(even_numbers)