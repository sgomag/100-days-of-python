from turtle import Turtle

def draw_net():
    net = Turtle()
    net.color("white")
    net.hideturtle()
    net.penup()
    net.goto(0, 300)
    while net.ycor() > -300:
        net.pendown()
        net.sety(net.ycor()-20)
        net.penup()
        net.sety(net.ycor() - 10)