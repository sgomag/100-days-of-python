from turtle import Turtle

INITIAL_SPEED = 0.005

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition(0,0)
        self.direction_x = 1
        self.direction_y = 1
        self.move_speed = INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.direction_x
        new_y = self.ycor() + self.direction_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.direction_y *= -1

    def bounce_x(self):
        self.direction_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.move_speed = INITIAL_SPEED
        self.direction_x *= -1