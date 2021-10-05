from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()  # calls super class' init
        self.shape("circle")    # Food class now has/knows all the methods from the Turtle class
        self.color("white")
        self.penup()
        self.x_move = 10    # starts out at 10, increase by 10
        self.y_move = 10    # starts out at 10, increase by 10
        self.move_speed = 0.1   # a number we put into time.sleep (the smaller the higher speed, cannot be less than 0)

    def move(self):
        """Increases x and y coordinates by 10 and moves the ball to the new position."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Wall bounce - changes y direction to an opposite of what it currently is, from 10 to - 10 and vice versa."""
        self.y_move *= -1   # it changes the direction, needs to be the opposite of what it currently is

    def bounce_x(self):
        """Paddle bounce - changes x direction to an opposite of what it currently is, from 10 to - 10 and vice versa."""
        self.x_move *= -1   # it changes the direction, needs to be the opposite of what it currently is
        self.move_speed *= 0.9  # lower the speed number for time.sleep, makes ball go faster

    def reset_position(self):
        """Resets position of the ball, resets its speed, changes balls direction."""
        self.goto(0, 0)     # back to the middle
        self.move_speed = 0.1   # resets the ball speed back to original
        self.x_move *= -1   # direction change, player take turn with the first bounce

