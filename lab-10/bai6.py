userInput = input("Input sequence: ")

newList = [*userInput]

result = {}

for i in newList:
    result[i] = newList.count(i)

print(result)