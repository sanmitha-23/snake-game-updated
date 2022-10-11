from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.bgcolor('black')
screen.tracer(0)

# creating a snake
my_snake = Snake()
# creating food object
food = Food()
# creating a score board object
score = Score()

screen.listen()
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.right, 'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    # detecting collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.add_score()

    # detect collision with wall
    if (my_snake.head.xcor() < -280) or (my_snake.head.xcor() > 280) or (my_snake.head.ycor() < -280) or \
            (my_snake.head.ycor() > 280):
        score.reset_game()
        my_snake.reset_game()

    # detect collision with tail
    for segment in my_snake.segments[1:]:   # slicing
        if my_snake.head.distance(segment) < 10:
            score.reset_game()
            my_snake.reset_game()


screen.exitonclick()
