from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.seth(0)
    tim.forward(50)

def move_backward():

    tim.backward(50)

def move_counter_clockwise():
    tim.right(10)
    tim.forward(100)

def move_clockwise():
    tim.left(10)
    tim.forward(100)


def clear_drawing():
    tim.clear()
    tim.setpos(0,0)
    tim.seth(0)


screen.listen()

screen.onkey(key = 'w', fun = move_forward)
screen.onkey(key = 's', fun = move_backward)
screen.onkey(key = 'a',fun = move_counter_clockwise)
screen.onkey(key = 'd', fun = move_clockwise)
screen.onkey(key = 'c', fun = clear_drawing)
screen.exitonclick()
