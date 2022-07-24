from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width = 640, height = 640)
screen.bgcolor('black')
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
def game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.06)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 14:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
            scoreboard.game_over()
            snake.reset()
            food.refresh()
            screen.onkeypress(game, 'r')
            time.sleep(1)
            scoreboard.clear()

        for segment in snake.segments[1:]:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                snake.reset()
                food.refresh()
                screen.onkeypress(game, 'r')


screen.onkeyrelease(game, 's')
screen.listen()


screen.exitonclick()