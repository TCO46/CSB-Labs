def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

user_input = int(input("Input number: "))

prime_number = 2

loop = 1

while loop <= user_input:
    if is_prime(prime_number):
        print(prime_number)
        loop += 1
    prime_number += 1
