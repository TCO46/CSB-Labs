def is_even(number):
    if number % 2 == 0:
        return True
    return False

user_input = int(input("Input a number: "))

if is_even(user_input):
    print("This number is even")
else:
    print("This number is not even")