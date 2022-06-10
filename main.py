from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
board = ScoreBoard()
screen.update()
game_is_on = True
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting distance between food and snake
    if snake.head.distance(food) <= 15:
        food.refresh()
        board.increase_score()
        board.update_score()
        snake.increase_length()

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        snake.reset()
        board.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset()

screen.exitonclick()
