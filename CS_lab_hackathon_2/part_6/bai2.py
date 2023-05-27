town_name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
population = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]

average_density_list = []

for i in range(len(population)):
    population_density = population[i] / area[i]
    average_density_list.append(population_density)

print(f"Average population density: {sum(average_density_list) / len(average_density_list)}")
