# import os
# import msvcrt
import random

# os.system("cls")
# ch = msvcrt.getch().decode('utf-8')

def map_render():
    values = ["P", "K", "D"]
    rows = 5
    cols = 10
    global array_2d
    array_2d = [["-" for _ in range(cols)] for _ in range(rows)]

    for value in values:
        while True:
            i = random.randint(0, rows - 1)
            j = random.randint(0, cols - 1)
            if array_2d[i][j] == "-":
                array_2d[i][j] = value
                break
map_render()

for row in array_2d:
    print(' '.join(row))
