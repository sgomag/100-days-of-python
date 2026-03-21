from turtle import Turtle

def draw_roads():
    road = Turtle()
    road.color("gray")
    road.hideturtle()
    road.penup()
    road.goto(-300,-245)

    while road.ycor() < 280:
        while road.xcor() < 300:
            road.pendown()
            road.setx(road.xcor() + 20)
            road.penup()
            road.setx(road.xcor() + 10)
        road.goto(-300, road.ycor() + 30)