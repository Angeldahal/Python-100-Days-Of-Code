from turtle import Turtle, Screen
import random 

def finishing_line():
    tim = Turtle()
    tim.pu()
    tim.setpos(x = 245, y = 400)
    tim.seth(-90)
    tim.pd()
    tim.pensize(5)
    tim.color("red")
    tim.forward(500)
    tim.hideturtle()

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = 'Make your bet', prompt = "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan","violet","Olive"]
turtles = []
n = 0
finishing_line()
for i in colors:
    turtles.append(Turtle())
    turtles[n].pu()
    turtles[n].color(i)
    turtles[n].shape('turtle')
    turtles[n].goto(x = -230, y = -100 + n * 40)
    n += 1

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")


screen.exitonclick()