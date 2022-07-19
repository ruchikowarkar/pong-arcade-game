from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(0.75, 2.75)
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(position, 10)

    def move_up(self):
        self.forward(50)

    def move_down(self):
        self.backward(50)