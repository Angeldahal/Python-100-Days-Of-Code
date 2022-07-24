import turtle as t
import random
from turtle import Screen

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.shape('turtle')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


for i in range(0,100):
    tim.color(random_color())
    tim.circle(100)
    tim.seth(i*5)










screen = Screen()
screen.exitonclick()