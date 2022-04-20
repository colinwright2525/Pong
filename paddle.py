from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.goto(coord)
        self.setheading(UP)
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed('fastest')

    def up(self):
        self.setheading(UP)
        self.forward(40)

    def down(self):
        self.setheading(DOWN)
        self.forward(40)

