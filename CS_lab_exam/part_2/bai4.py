from turtle import *

edges = int(input("Input number of edges: "))

for _ in range(edges):
    forward(100)
    right(360/edges)
done()