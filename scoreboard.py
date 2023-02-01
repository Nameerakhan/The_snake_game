from turtle import Turtle
ALIGHNMENT = "center"
FONT = ("Arial", 24, "normal")
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"Score:{self.score}", align=ALIGHNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGHNMENT, font=FONT)
    def increase(self):
        self.score+=1
        self.clear()
        self.score_update()

