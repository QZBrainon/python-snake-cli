#!/usr/bin/python

from curses import wrapper
from snake import Snake
from food import Food
from window import Window
from settings import Settings
from directions import Directions


def main(screen):
    # settings of the game
    window = Window(screen)
    config = Settings(screen)
    window.title('Python Snake CLI')
    window.draw_border()
    config.show_cursor(False)
    config.no_delay(True)
    config.timeout(150)

    snk = Snake(window)
    window.draw(snk)
    direction = Directions.RIGHT.value
    

    food = Food.generate_food(snk, window) # creates and set the first food on the board
    Food.draw_food(food, screen)

    while True:
        key = screen.getch() # waits for user to press a key, since no_delay is true, it starts after the specified timeout
        if key in [Directions.RIGHT.value, Directions.LEFT.value, Directions.UP.value, Directions.DOWN.value]: # make sure the input is a valid direction
            direction = key

        snk.move(direction)
        window.animate(snk)

        # checks if the snake ate the food, generates another if so, if not just pop the tail to keep moving 
        if food == snk.body[0]:
            food = Food.generate_food(snk, window)
            Food.draw_food(food, screen)
        else:
            snk.body.pop()

        # checks the exit condition
        if snk.touches_border(window) or snk.touches_itself():
            window.end_game()
            break

        screen.refresh()

wrapper(main)