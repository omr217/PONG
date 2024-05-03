from turtle import Screen
from pedal import Pedal
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)

l_pedal = Pedal((-350, 0))
r_pedal = Pedal((350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.onkey(l_pedal.go_up, "w")
screen.onkey(l_pedal.go_down, "s")
screen.onkey(r_pedal.go_down, "Down")
screen.onkey(r_pedal.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_pedal) < 50 or ball.xcor() < -320 and ball.distance(l_pedal) < 50:
        ball.bounce_x()

    if ball.xcor() > 420:
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -420:
        ball.reset_position()
        score_board.r_point()

















screen.exitonclick()