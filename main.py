from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
import time

# Code for screen of game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)  # Animation of screen gets off


right_paddle = Paddle()
left_paddle = Paddle()
ball = Ball()
score = Score()

# Create right and left paddle
right_paddle.paddle(350, 0)
left_paddle.paddle(-350, 0)

# Onkey is used to move the paddle up and down
screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    r_pos = right_paddle.position()
    ball.move()

    # Detect the collision with horizontal walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect the collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.x_bounce()

    # Detect if ball missing the right paddle
    if ball.xcor() > 410:
        ball.reset_position()
        score.update_r_score()

    # Detect if ball missing the left paddle
    if ball.xcor() < -410:
        ball.reset_position()
        score.update_l_score()


screen.exitonclick()
