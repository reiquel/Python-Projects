from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self, position):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
    
    def down(self):
        self.head.setheading(270)
    
    def left(self):
        self.head.setheading(180)
    
    def right(self):
        self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1500,1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]