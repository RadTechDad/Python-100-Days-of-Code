import random
import tkinter.constants
import turtle
from random import choices

from turtle import Turtle, Screen


# Functions
def draw_line(turtle, distance=100, line_seg=5, space_seg=5):
    pos = 0

    while pos < distance:
        turtle.forward(line_seg)
        pos += line_seg
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()
        turtle.forward(space_seg)
        pos += space_seg
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()

def draw_shape(turtle, segment, sides):
    for _ in range(sides):
        turtle.right(360/sides)
        turtle.forward(segment)

def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def graphics_start():
    screen = Screen()
    screen.register_shape("python.gif")
    screen.colormode(255)
    screen.listen()

def graphics_end():
    screen.exitonclick()

# Main
segment_length = 50
line_thickness = 20
# 0 - fastest | >10 or <0.5 == 0
# 1 - slowest
# 3 - slow
# 6 - normmal
# 10 - fast
draw_speed = 6


t = Turtle()
t.shape("python.gif")

# Get into starting position
t.teleport(t.xcor() + (segment_length // 2), t.ycor() + (segment_length * 2))

for sides in range(3,21):
    t.pencolor(random_rgb_color())
    draw_shape(t, segment_length, sides)


def main():
    print("Hello from test!")


if __name__ == "__main__":
    main()
