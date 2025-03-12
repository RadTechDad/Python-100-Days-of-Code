import random
import os

from turtle import Turtle, Screen

def main():

    #####
    # Functions
    ####################
    def graphics_start():
        screen.title(os.path.basename(__file__))
        screen.setup(500, 500)
        screen.register_shape(python_shape)
        monty.shape(python_shape)
        screen.listen()

        # Get into starting position
        monty.teleport(monty.xcor() + (segment_length // 2), monty.ycor() + (segment_length * 2))

        monty.speed(draw_speed)

    def graphics_end():
        screen.exitonclick()

    def random_rgb_color():
        screen.colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    def draw_line(seg_length=100, line_thickness=1, color=(0,0,0)):
        monty.width(line_thickness)
        monty.pencolor(color)
        monty.forward(seg_length)

    def draw_shape(seg_length=100, shape_sides=4, line_thickness=1, color=(0,0,0)):
        for _ in range(shape_sides):
            monty.right(360 / shape_sides)
            draw_line(seg_length, line_thickness, color)

    #####
    # Variables
    ####################
    color_set_1 = [ "royal blue", "deep sky blue", "turquoise", "forest green", "dark green", "deep pink", "hot pink", "red", "dark orange", "gold" ]
    color_set_2 = [ "purple", "medium purple", "dark violet", "magenta", "tomato", "firebrick", "chocolate", "dark goldenrod", "olive drab", "slate blue" ]

    segment_length = 100
    line_width = 2
    draw_speed = 'fast'
    python_shape = os.path.join("../", "img/", "python.gif")

    #####
    # Main
    ####################
    screen = Screen()
    monty = Turtle()

    graphics_start()

    for sides in range(3,10):
        draw_shape(segment_length, sides, line_width, random_rgb_color())

    graphics_end()






if __name__ == "__main__":
    main()
