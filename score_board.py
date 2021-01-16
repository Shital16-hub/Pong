from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 250)
        self.write(self.l_score, move=False, align="left", font=("Arial", 28, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, move=False, align="left", font=("Arial", 28, "normal"))

    def update_l_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()




