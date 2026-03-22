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
        # Fetch highest score from data.txt
        with open("data.txt", mode="r") as data:
            self.highest_score = int(data.read())
        self.show_scoreboard()

    def add_point(self):
        self.score += 1
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            self.highest_score = self.score
        self.score = 0
        self.show_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)
