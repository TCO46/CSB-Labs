import random

print("== FREAKING MATH CONSOLE ==")

score = 0
while(True):

    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)

    operators = random.choice(['+', '-', '*'])

    result = int(input(f"{number1} {operators} {number2} = "))

    if(operators == "+"):
        problem = number1 + number2
    elif(operators == "-"):
        problem = number1 - number2
    elif(operators == "*"):
        problem = number1 * number2


    if(problem == result):
        score+=1
        print(score)
    else:
        print("== GAME OVER ==")
        print(f"Your total score is {score}")
        break
