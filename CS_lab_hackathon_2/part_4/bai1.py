numbers = [53, 85, 96, 76, 8, 62, 58]

even_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])

print(even_numbers)
