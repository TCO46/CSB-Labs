def is_palidrome(string):
    if string == string[::-1]:
        return True
    return False

user_input = input("Input a text: ")

if is_palidrome(user_input):
    print("This is a palidrome")
else:
    print("This is not a palidrome")