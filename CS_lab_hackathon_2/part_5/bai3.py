town_name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
population = [247100, 333300, 266800, 420900, 318000]

max = min = population[0]

max_positon = min_position = 0

for i in range(len(population)):
    if population[i] > max:
        max = population[i]
        max_positon = i
    if population[i] < min:
        min = population[i]
        min_position = i

print(f"most population: {town_name[max_positon]}")
print(f"least population: {town_name[min_position]}")

