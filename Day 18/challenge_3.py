from turtle import Turtle, Screen
import random

color = ['red',
         'orange',
         'yellow',
         'green',
         'blue',
         'indigo',
         'violet',
         'purple',
         'pink',
         'silver',
         'gold',
         'beige',
         'brown',
         'grey',
         'black',
         'white']

tim = Turtle()
tim.shape('turtle')
tim.color('black')
tim.speed(1)
for i in range(3, 15):
    rot_angle = 360 / i
    count = 0
    n = i
    tim.color(random.choice(color))
    do_continue = True
    while do_continue:
        tim.seth(count + rot_angle)
        tim.forward(50)
        count += rot_angle
        n -= 1
        if n == 0:
            do_continue = False

screen = Screen()
screen.exitonclick()
