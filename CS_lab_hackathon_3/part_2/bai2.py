def min_to_max(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

print(min_to_max([5, 1, 8, 92, -1, 30]))
