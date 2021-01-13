from turtle import Turtle


class Paddle(Turtle):
    def paddle(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_position, y_position)

    def paddle_up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)


