import random
import os

from turtle import Turtle, Screen
####################



def main():

    #####
    # Functions
    ####################
    def graphics_start():
        screen.title(os.path.basename(__file__))
        screen.setup(window_dimension, window_dimension)

        monty.hideturtle()
        monty.speed(draw_speed)

        screen.listen()

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

    def draw_spiralgraph():
        for a in range(number_of_circles):
            monty.pencolor(random_rgb_color())
            monty.circle(circle_radius)
            monty.tilt(360 / number_of_circles)
            monty.setheading(monty.tiltangle())


    #####
    # Variables
    ####################
    color_set_1 = [ "royal blue", "deep sky blue", "turquoise", "forest green", "dark green", "deep pink", "hot pink", "red", "dark orange", "gold" ]
    color_set_2 = [ "purple", "medium purple", "dark violet", "magenta", "tomato", "firebrick", "chocolate", "dark goldenrod", "olive drab", "slate blue" ]

    window_dimension = 500
    max_diameter = window_dimension-4

    draw_speed = 'fastest'
    circle_radius = 100
    number_of_circles = 36


    #####
    # Main
    ####################
    screen = Screen()
    monty = Turtle()

    graphics_start()

    draw_spiralgraph()

    graphics_end()



####################
if __name__ == "__main__":
    main()

