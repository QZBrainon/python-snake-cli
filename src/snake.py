from directions import Directions
from window import Window

class Snake():
    def __init__(self, window: Window) -> None:
        self.body = [ [window.heigth//2, window.width//2 +1], [window.heigth//2, window.width//2], [window.heigth//2, window.width//2 -1] ] # coordinates related to the screen. Positions it in the center
        self.direction = Directions.RIGHT.value
        self.last_direction = Directions.RIGHT.value

    def right(self):
        self.last_direction = Directions.RIGHT.value
        self.body.insert(0, [self.body[0][0], self.body[0][1]+1])

    def left(self):
        self.last_direction = Directions.LEFT.value
        self.body.insert(0, [self.body[0][0], self.body[0][1]-1])

    def up(self):
        self.last_direction = Directions.UP.value
        self.body.insert(0, [self.body[0][0]-1, self.body[0][1]])

    def down(self):
        self.last_direction = Directions.DOWN.value
        self.body.insert(0, [self.body[0][0]+1, self.body[0][1]])

    def move(self, direction: Directions):
        if direction == Directions.RIGHT.value and self.last_direction != Directions.LEFT.value or direction == Directions.LEFT.value and self.last_direction == Directions.RIGHT.value:
            self.right()
        elif direction == Directions.LEFT.value and self.last_direction != Directions.RIGHT.value or direction == Directions.RIGHT.value and self.last_direction == Directions.LEFT.value:
            self.left()
        elif direction == Directions.UP.value and self.last_direction != Directions.DOWN.value or direction == Directions.DOWN.value and self.last_direction == Directions.UP.value:
            self.up()
        elif direction == Directions.DOWN.value and self.last_direction != Directions.UP.value or direction == Directions.UP.value and self.last_direction == Directions.DOWN.value:
            self.down()

    
    def touches_border(self, window):
        if self.body[0][0] in [window.border[0][0], window.border[1][0]] or self.body[0][1] in [window.border[0][1], window.border[1][1]] or self.body[0] in self.body[1:]:
            return True
        
    def touches_itself(self):
        if self.body[0] in self.body[1:]:
            return True