number = int(input("Input a number: "))
num1 = 1
num2 = 1

for i in range(number):
    print(num1, end=" ")
    res = num1 + num2
    num1 = num2
    num2 = res
