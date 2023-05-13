number = int(input("Input a number: "))
number+=1

i = 0

for i in range(number):
    if(i % 2 != 0):
        print(i, end=" ")
        i+=1