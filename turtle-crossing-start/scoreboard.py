FONT = ("Courier", 24, "normal")
ALINGMENT = "center"
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 260)
        self.write(f"Level: {self.level}", align="center", font=(FONT))
    
    def game_over(self):
        self.goto(0, 20)
        self.write("GAME OVER", align=ALINGMENT, font=FONT)

    def point(self):
        self.level += 1
        self.update_scoreboard()

