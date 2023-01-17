import random
from turtle import *
import math

def dum(a):
    left(90)
    forward(a)
    right(90)
    forward(a)
    right(45 + 90)
    forward(math.sqrt(a**2 * 2))
    left(45 + 90)
    forward(a)
    left(90)
    forward(a)
    left(45)

    forward(math.sqrt(a**2 / 2))
    left(90)
    forward(math.sqrt(a**2 * 2) / 2)
    left(90)
    forward(math.sqrt(a**2 * 2))
    left(45)

penup()
goto(-400, 0)
pendown()
for i in range(12):
    dum(70)
    forward(10)


exitonclick()