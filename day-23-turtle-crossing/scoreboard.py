from turtle import Turtle

FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-260,270)
        self.color("white")
        self.level = 1
        self.show_scoreboard()

    def upgrade_level(self):
        self.clear()
        self.level += 1
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"Level: {self.level}", align = "left", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
