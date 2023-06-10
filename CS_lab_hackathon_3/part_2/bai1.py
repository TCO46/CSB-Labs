def fact(number):
    for i in range(1, number):
        number = number*i
    return number

user_input = int(input("Input a number: "))

print(f"{user_input}! = {fact(user_input)}")