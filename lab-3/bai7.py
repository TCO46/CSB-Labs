a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))

from turtle import *

if pow(a, 2) == pow(b, 2) + pow(c,2) or pow(b, 2) == pow(a, 2) + pow(c,2) or pow(c, 2) == pow(b, 2) + pow(a,2):
    print("The 3 line segments can form a right triangle.")
elif a == b == c:
    print("The 3 line segments can form an equilateral triangle.")
elif a+b>c and b+c>a and c+a>b:
    print("The 3 line segments can form a triangle.")
else:
    print("The 3 line segments cannot form a triangle.")
