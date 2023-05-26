arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Original list: {arr}")

add2 = []
time2 = []

for i in range(len(arr)):
    add2.append(arr[i]+2)
for i in range(len(arr)):
    time2.append(arr[i]*2)
for i in range(2):
    x = arr.pop(0)
    arr.insert(len(arr), x)

print(f"Add2: {add2}")
print(f"Multiply by 2: {time2}")
print(f"Shift 2: {arr}")
