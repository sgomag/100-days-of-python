from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0,0), (-20,0),(-40,0)]

segments = []

for position in starting_positions:
    seg = Turtle("square")
    seg.color("white")
    seg.penup()
    seg.shapesize(0.9,0.9)
    seg.setposition(position)
    segments.append(seg)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_i in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_i -1].xcor()
        new_y = segments[seg_i -1].ycor()
        segments[seg_i].goto(new_x, new_y)
    segments[0].forward(20)






screen.exitonclick()