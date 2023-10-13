from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_one.go_up, "Up")
screen.onkey(paddle_one.go_down, "Down")
screen.onkey(paddle_two.go_up, "w")
screen.onkey(paddle_two.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_moving()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
