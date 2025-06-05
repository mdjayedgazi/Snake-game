from turtle import Turtle

ALIGNMENT = "center"
FONT =("Arial",20,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,265)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.clear()
        self.write(f"Game is Over! \n\nYour Score is {self.score}",move=False,align=ALIGNMENT, font=("Arial",15,"normal"))


    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
