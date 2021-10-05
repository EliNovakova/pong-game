from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # calls super class' init
        self.color("white")
        self.penup()
        self.hideturtle()   # to hide the turtle arrow
        self.l_score = 0    # score at the beginning
        self.r_score = 0    # score at the beginning
        self.update_scoreboard()    # writes score

    def update_scoreboard(self):
        """To write the score (if in init, writes only once)."""
        self.goto(-100, 200)    # l_score position
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)     # r_score position
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        """Adds 1 point to a l_player and updates/writes score."""
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Adds 1 point to a r_player and updates/writes score."""
        self.clear()
        self.r_score += 1
        self.update_scoreboard()