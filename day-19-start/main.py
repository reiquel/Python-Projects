from turtle import Turtle, Screen


tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def move_counter_clockwise():
    tim.left(90)

def move_clockwise():
    tim.right(90)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


    
screen.listen()
move_forward = screen.onkey(key="w", fun=move_forward)
move_backward = screen.onkey(key="s", fun=move_backward)
move_counter_clockwise = screen.onkey(key="a", fun=move_counter_clockwise)
move_clockwise = screen.onkey(key="d", fun=move_clockwise)
clear_drawing = screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()