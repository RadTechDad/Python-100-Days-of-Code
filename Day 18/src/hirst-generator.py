import os.path
import colorgram
import json
import random
from turtle import Turtle, Screen

def main():
    #####
    # Functions
    ####################
    def init(palette):
        img = os.path.join(IMAGE_FOLDER, PALETTE_IMAGE)

        if os.path.exists(JSON_DATA_FILE):  # Load json data if exists
            palette.extend(load_color_dict_from_json())
        else: # If json data doesn't exist, create it
            monty.penup()
            monty.sety(monty.ycor()-50)
            monty.write(f"Colors not cached. Please wait while we calculate the colors from", align='center', font=('Arial', 14, 'normal'))
            monty.sety(monty.ycor()-30)
            monty.write(f"\"{PALETTE_IMAGE}\".", align='center', font=('Courier New', 14, 'normal'))
            monty.home()
            color_list = generate_color_list_from_image(img)

            save_color_dict_to_json(color_list_to_color_dict(color_list))
            print(f"Colors cached to \"{JSON_DATA_FILE}\".")

            palette.extend(color_list)
            screen.reset()

        monty.speed(DRAW_SPEED)

    def graphics_start():
        img = os.path.join(IMAGE_FOLDER, TURTLE_SHAPE_IMAGE)
        screen.title(os.path.basename(__file__))
        screen.setup(WINDOW_SIZE, WINDOW_SIZE)
        screen.register_shape(img)
        monty.shape(img)
        screen.listen()
        monty.speed(DRAW_SPEED)

    def graphics_end():
        screen.exitonclick()

    def generate_color_list_from_image(image):
        try:
            colors = colorgram.extract(image, PALETTE_SIZE)
        except FileNotFoundError:
            print(f"** ERROR: {image} not found. **")
            exit(13)

        list_of_colors = []
        for color in colors:
            list_of_colors.append(tuple(color.rgb))

        return list_of_colors

    def color_list_to_color_dict(list_data):
        color_dict = {}
        index = 1

        for color in list_data:
            r, g, b = color
            color_key = "Color " + str(index)
            color_dict[color_key] = { 'r':r, 'g':g, 'b':b}
            index += 1

        return color_dict

    def color_dict_to_color_list(dict_data):
        color_list = []

        for rgb_values in dict_data.values():
            color_list.append((rgb_values['r'], rgb_values['g'], rgb_values['b']))

        return color_list

    def load_color_dict_from_json():
        try:
            with open(JSON_DATA_FILE, 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            print(f"** ERROR: '{JSON_DATA_FILE}' not found! **")

        return color_dict_to_color_list(data)

    def save_color_dict_to_json(dict_data):
        try:
            with open(JSON_DATA_FILE, 'w', encoding='utf-8') as file:
                # noinspection PyTypeChecker
                json.dump(dict_data, file, indent = 4)
        except FileExistsError:
            print(f"** ERROR: '{JSON_DATA_FILE}' already exists.")
            exit(13)

    def random_pal_color():
        screen.colormode(255)
        return random.choice(color_palette)

    def draw_dot_matrix():
        monty.penup()
        starty = monty.ycor() + (DOT_SIZE // 2)
        startx = monty.xcor() + (DOT_SIZE // 2)
        for ypos in range(DOT_MATRIX_SIZE):
            monty.sety(starty + (ypos * (DOT_SIZE + DOT_SPACING)))
            for xpos in range(DOT_MATRIX_SIZE):
                monty.setx(startx + (xpos * (DOT_SIZE + DOT_SPACING)))
                monty.pendown()
                # print(f"Monty: ({monty.pos()}) | Visible? {monty.isvisible()} | Pen down? {monty.isdown()} | Color: {c}")
                monty.dot(DOT_SIZE, random_pal_color())
                monty.penup()
            monty.setx(startx)



    #####
    # CONSTANTS
    ####################
    IMAGE_FOLDER = '../img'
    PALETTE_IMAGE = 'pexels-pixabay-207725.jpg'
    TURTLE_SHAPE_IMAGE = 'python.gif'
    JSON_DATA_FILE = 'color-palette.json'

    PALETTE_SIZE = 30

    DRAW_SPEED = 'fastest'

    DOT_SIZE = 20
    DOT_SPACING = 50
    DOT_MATRIX_SIZE = 10    # Meaning 10x10 matrix

    CANVAS_PADDING = 0
    CANVAS_SIZE = (DOT_SIZE * DOT_MATRIX_SIZE) + (DOT_SPACING * (DOT_MATRIX_SIZE - 1)) + (CANVAS_PADDING * 2)

    WINDOW_PADDING = 50
    WINDOW_SIZE = CANVAS_SIZE + (WINDOW_PADDING * 2)



    #####
    # Variables
    ####################
    screen = Screen()
    monty = Turtle()
    color_palette = []



    #####
    # Main
    ####################
    graphics_start()
    init(color_palette)

    monty.teleport((-CANVAS_SIZE//2),(-CANVAS_SIZE//2))

    draw_dot_matrix()

    graphics_end()


#####
# Invoker
####################
if __name__ == "__main__":
    main()