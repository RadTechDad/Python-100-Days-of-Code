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

        squiggles.hideturtle()
        squiggles.speed('fastest')
        squiggles.teleport(200, -220)

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


    #####
    # Variables
    ####################
    directions = [ 0, 90, 180, 270 ]
    color_set_1 = [ "royal blue", "deep sky blue", "turquoise", "forest green", "dark green", "deep pink", "hot pink", "red", "dark orange", "gold" ]
    color_set_2 = [ "purple", "medium purple", "dark violet", "magenta", "tomato", "firebrick", "chocolate", "dark goldenrod", "olive drab", "slate blue" ]

    window_dimension = 500
    segment_length = 25
    line_thickness = 10
    draw_speed = 'fastest'
    iterations = 100


    #####
    # Main
    ####################
    screen = Screen()
    monty = Turtle()
    squiggles = Turtle()

    graphics_start()

    for x in range(iterations):
        monty.setheading(random.choice(directions))
        # draw_line(segment_length, line_thickness, random.choice(color_set_1))
        draw_line(segment_length, line_thickness, random_rgb_color())
        squiggles.clear()
        squiggles.write("Iterations: " + str(x + 1), align="right", font=('Arial', 14, 'normal'))

    graphics_end()



####################
if __name__ == "__main__":
    main()

