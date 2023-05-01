import curses

class Settings():
    def __init__(self, screen) -> None:
        self.screen = screen

    def show_cursor(self, enable_cursor: bool = True) -> None:
        curses.curs_set(enable_cursor)

    def no_delay(self, delay: bool = False) -> None:
        self.screen.nodelay(delay)

    def timeout(self, ms: int) -> None:
        self.screen.timeout(ms)
        