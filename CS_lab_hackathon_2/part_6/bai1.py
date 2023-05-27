town_name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
population = [247100, 333300, 266800, 420900, 318000]
area = [9.224, 43.35, 12.04, 9.96, 10.09]

for i in range(len(population)):
    print(f"-{town_name[i]}: {population[i] / area[i]}")
