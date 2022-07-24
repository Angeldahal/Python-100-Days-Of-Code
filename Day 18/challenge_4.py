from turtle import Turtle as t, Screen
import random

tim = t()
tim.color('cyan')
tim.shape('turtle')
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(15)
tim.speed('fast')
for i in range(200):
    tim.color(random.choice(colours))
    tim.seth((random.randint(1, 4))*90)
    tim.forward(50)















screen = Screen()
screen.exitonclick()
