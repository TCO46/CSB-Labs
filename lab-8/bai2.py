user_input = int(input("Input number: "))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if is_prime(user_input) == True:
    print(f"{user_input} is a prime number")
else:
    print(f"{user_input} is not a prime number")


