from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    # controls animation, turns it off

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")  # right paddle up
screen.onkey(r_paddle.go_down, "Down")  # right paddle down
screen.onkey(l_paddle.go_up, "w")   # left paddle up
screen.onkey(l_paddle.go_down, "s") # left paddle down

game_is_on = True
while game_is_on:
    screen.update()      # manually refreshes screen, has to be updated in a while loop
    time.sleep(ball.move_speed)  # to slow the animation, to delay the refresh
    ball.move()     # makes the ball move, changes its coordinates

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:     # if its to far up or to far down
        ball.bounce_y()   # has to bounce

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # if ball and paddle are close (measured from the center therefore 50 - paddle is 100 long)
        # AND if ball has x coordinate of the x coordinate of the paddle
        ball.bounce_x()     # has to bounce

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()    # to add a point to l_player if r_player misses

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()    # to add a point to r_player if l_player misses


screen.exitonclick()


