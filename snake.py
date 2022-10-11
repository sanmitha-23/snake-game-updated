from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]   # making it constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """create a snake"""
        for position in POSITIONS:
            self.add_seg(position)

    def add_seg(self, position):
        new_turtle = Turtle()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        """move the snake"""
        for snake in range(len(self.segments) - 1, 0, -1):  # start stop step
            new_x = self.segments[snake - 1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_game(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
