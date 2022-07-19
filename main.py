from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-470)
r_paddle = Paddle(470)
ball = Ball()
r_score = Scoreboard(100)
l_score = Scoreboard(-100)

partition = Turtle()
partition.color("white")
partition.shape("square")
partition.pensize(5)
partition.penup()
partition.goto(0, 280)
partition.right(90)
for i in range(19):
    partition.pendown()
    partition.forward(15)
    partition.penup()
    partition.forward(15)
partition.hideturtle()

screen.update()
screen.tracer(1)

if ball.xcor() > 0:
    screen.listen()
    screen.onkey(key="Up", fun=l_paddle.move_up)
    screen.onkey(key="Down", fun=l_paddle.move_down)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    ball.ball_move()

    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.reverse()
        r_score.increase_score()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reverse()
        l_score.increase_score()
    if ball.xcor() >= 480 or ball.xcor() <= -480:
        ball.reset()

screen.exitonclick()
