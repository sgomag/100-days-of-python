from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Create instances
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

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
    time.sleep(0.005)
    ball.move()

    #Detect collision with top or bottom screen edge. Ball radius is 10.
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    #Detect collision with paddle. Distance from the center of the paddle to its corner is 51.
    if ball.distance(r_paddle) < 51 and ball.xcor() == 340 or ball.distance(l_paddle) < 51 and ball.xcor() == -340:
        ball.bounce_x()

    #Detect when right paddle misses the ball
    if ball.xcor() > 380:
        game_is_on = False

screen.exitonclick()