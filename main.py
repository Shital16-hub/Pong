from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle()
left_paddle = Paddle()
right_paddle.paddle(350, 0)
left_paddle.paddle(-350, 0)

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()