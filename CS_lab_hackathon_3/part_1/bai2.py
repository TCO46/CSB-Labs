def cal_area(radius):
    return 3.14*pow(radius, 2)

user_input = int(input("Input radius: "))

print(f"Circle's area: {cal_area(user_input)}")