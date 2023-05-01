import curses
from curses.textpad import rectangle

class Window():
    def __init__(self, screen, border_offset:int = 3) -> None:
        self.screen = screen
        self.heigth = curses.LINES - 1
        self.width = curses.COLS - 1
        self.top = [ i for i in range(self.width + 1)]
        self.right = [i for i in range(self.width, self.heigth + 1)]
        self.left = [ i for i in range(self.heigth + 1)]
        self.bottom = [i for i in range(self.heigth, self.width + 1)]
        self.border = [[border_offset, border_offset],[self.heigth-border_offset, self.width-border_offset]]

    def draw_border(self) -> None:
        rectangle(self.screen, self.border[0][0], self.border[0][1], self.border[1][0], self.border[1][1]) # draws the white lines to make the border inside the window


    def title(self, title: str) -> None:
        self.screen.addstr(0, self.width//2, title)


    def draw(self, snake):
        for y, x in snake.body:
            self.screen.addstr(y, x, '#')

    def animate(self, snake):
        head = snake.body[0]
        tail = snake.body[-1]
        self.screen.addstr(head[0], head[1], '#')
        self.screen.addstr(tail[0], tail[1], ' ')


    def end_game(self):
        msg = 'Game Over!'
        self.screen.addstr(self.heigth//2, self.width//2, msg)
        self.screen.nodelay(False)
        self.screen.getch()