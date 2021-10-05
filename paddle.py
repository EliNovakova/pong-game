from turtle import Turtle


class Paddle(Turtle):   # inherits from Turtle class

    def __init__(self, position):   # we have to type in a tuple (coordinates) when creating an object from this class
        super().__init__()  # calls super class' init
        self.shape("square")   # all turtles start off by 20x20
        self.shapesize(stretch_wid=5, stretch_len=1)  # stretch width by 5, length leave as is, paddle is 100x20
        self.color("white")
        self.penup()
        self.goto(position) # sets position based on the tuple coordinates from argument

    def go_up(self):
        """Moves paddle up by 20 paces."""
        new_y = self.ycor() + 20  # new y which is 20 paces up from the original
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves paddle down by 20 paces."""
        new_y = self.ycor() - 20  # new y which is 20 paces down from the original
        self.goto(self.xcor(), new_y)