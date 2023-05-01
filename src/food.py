from random import randint

class Food():
    @staticmethod
    def generate_food(snake, window):
        food = None
        while food == None:
            food = [randint(window.border[0][0]+1, window.border[1][0]-1), randint(window.border[0][1]+1, window.border[1][1]-1)]
            if food in snake.body:
                food = None
        return food

    @staticmethod
    def draw_food(food, screen):
        screen.addstr(food[0], food[1], '*')
