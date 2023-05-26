import random

print("== FREAKING MATH CONSOLE ==")

score = 0
level = 0

while(True):
    operators = random.choice(['+', '-', '*'])

    if(level < 10):
        easy1 = random.randint(1, 5)
        easy2 = random.randint(1, 5)
        result = int(input(f"{easy1} {operators} {easy2} = "))
    elif(level < 20):
        medium1 = random.randint(1, 10)
        medium2 = random.randint(1, 10)
        result = int(input(f"{medium1} {operators} {medium2} = "))
    elif(level < 50):
        hard1 = random.randint(1, 50)
        hard2 = random.randint(1, 50)
        result = int(input(f"{hard1} {operators} {hard2} = "))


    if(operators == "+"):
        problem = number1 + number2
    elif(operators == "-"):
        problem = number1 - number2
    elif(operators == "*"):
        problem = number1 * number2

    if(problem == result):
        score+=1
        level+=1
        print(score)
    else:
        print("== GAME OVER ==")
        print(f"Your total score is {score}")
        break
