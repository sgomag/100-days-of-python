from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from net import draw_net

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create instances
draw_net()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

#Screen instructions
screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")

#Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with top or bottom screen edge. Ball radius is 10.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    #Detect collision with paddle. Distance from the center of the paddle to its corner is 54.
    if (ball.distance(r_paddle) < 54 and ball.xcor() == 330) or (ball.distance(l_paddle) < 54 and ball.xcor() == -330):
        ball.bounce_x()

    #Detect when right paddle misses the ball
    if ball.xcor() > 380:
        time.sleep(0.5)
        scoreboard.l_point()
        ball.reset()

    #Detect when right paddle misses the ball
    if ball.xcor() < -380:
        time.sleep(0.5)
        scoreboard.r_point()
        ball.reset()



screen.exitonclick()