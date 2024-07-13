from turtle import Turtle
ALINGMENT = "center"
FONT = ("Courier", 14, "normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("../../../Desktop/data.txt") as file:
           self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(-40, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALINGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../../Desktop/data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
    def keep_high_score(self):
        with open("../../../Desktop/data.txt",mode="w") as file:
            file.write(f"{self.high_score}")
    

        

