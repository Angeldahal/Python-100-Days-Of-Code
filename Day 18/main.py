import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
color_list = [(35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8)]
tim.speed(0)
tim.pu()
tim.setpos(-150,0)
tim.pd()
tim.hideturtle()
for i in range(0, 10):
    tp = tim.pos()
    for i in range(0, 10):
        tim.dot(20,color_list[random.randint(0,len(color_list)-1)])
        tim.penup()
        tim.forward(50)
    tim.setpos(tp)   
    tim.seth(90)
    tim.pu()
    tim.fd(50)
    tim.pd()
    tim.seth(0)



screen = t.Screen()
screen.exitonclick()
