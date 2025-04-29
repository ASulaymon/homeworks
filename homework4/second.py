from turtle import *
import random as r

tracer(9999)

while True:
    random = r.randint(0, 10)
    random2 = r.randint(0, 100)
    random3 = r.randint(0, 1000)
    forward(random)
    circle(random2)
    right(random3)