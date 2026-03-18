from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")
        self.score = 0
        self.show_scoreboard()

    def add_point(self):
        self.clear()
        self.score += 1
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
