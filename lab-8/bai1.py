user_input = input("Input number: ")

def is_int(number):
    if number.isdigit():
        return True
    else:
        return False

if is_int(user_input):
    print(f"{user_input} is an integer")
else:
    print(f"{user_input} is not an integer")

