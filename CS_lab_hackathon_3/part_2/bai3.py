def print_fibo(number):
    count = 0

    n1, n2 = 0, 1
    while count < number:
        result = n1 + n2
        n1 = n2
        n2 = result
        count+=1
        print(n1, end=" ")

user_input = int(input("Input a number: "))

print(f"First {user_input} Fibonacci numbers: ")
print_fibo(user_input)