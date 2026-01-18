from conway_grid import ConwayGrid
import curses

class ConwaySystem:
    def run_iteration(self):
        old_grid = self._game.get_grid_copy()

        for i in range(self._ey-self._by):
            for j in range(self._ex-self._bx):
                self._game.iterate_cell(old_grid, i, j)
    
    
    def update_screen(self, screen):
        for i in range(self._ey-self._by):
            for j in range(self._ex-self._bx):
                if self._game.get_cell(i, j) == 1:
                    screen.addstr(i+self._by, j+self._bx, "\u2588", curses.color_pair(2))
                else:
                    screen.addstr(i+self._by, j+self._bx, "\u2588", curses.color_pair(1))


    def paint(self, screen, y, x):
        cell = self._game.get_cell(y-self._by, x-self._bx)

        id_y, id_x = y-self._by, x-self._bx
        if cell == 0:
            self._game.set_cell(id_y, id_x, 1)
        else:
            self._game.set_cell(id_y, id_x, 0)

        self._cell = self._game.get_cell(y-self._by, x-self._bx)


    def __init__(self, y, x):
        self._ey, self._bx = ((y-4, x//8))
        self._by, self._ex = (4, x - self._bx)
        self._game = ConwayGrid(self._ey-self._by, self._ex-self._bx)

        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        self.refresh_rate = 60


