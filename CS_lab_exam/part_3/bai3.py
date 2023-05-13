number = int(input("Input a months: "))

if(number < 10 and number % 2 != 0):
    print("This month has 31 days")
elif(number >= 10 and number % 2 == 0):
    print("This month has 31 days")
else:
    print("This month has 30 days")
