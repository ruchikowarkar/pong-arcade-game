from turtle import Turtle
alignment = "center"
font = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position, 200)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, align=alignment, font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

