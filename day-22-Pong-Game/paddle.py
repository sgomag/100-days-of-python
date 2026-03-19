from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, initial_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setposition(initial_position)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)