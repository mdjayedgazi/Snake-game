from turtle import Turtle
import random


class Food(Turtle):  #Inheritance

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("pink")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,250)
        random_y = random.randint(-280,250)
        self.goto(x=random_x,y=random_y)

