from turtle import *

colors = ["purple", "blue", "pink", "green"]

pensize(5)

for i in range(len(colors)):
    pendown()
    color(colors[i])
    forward(30)
    penup()
    forward(30)

done()