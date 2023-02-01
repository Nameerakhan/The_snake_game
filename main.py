from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import score

import time
screen = Screen()
screen.setup(width=600,height = 600)
screen.bgcolor("white")
screen.title("The snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = score()
snake.create_snake()
screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Right,"Right")
screen.onkey(snake.Left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect the distance from food
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase(scoreboard)

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        score.game_over(scoreboard)

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
