from copy import deepcopy

class ConwayGrid:
    #class instancer
    def __init__(self, size_y, size_x):
        self._cols, self._rows = size_y, size_x
        self._grid = [[0 for j in range(size_x)] for i in range(size_y)]
    
    #void
    def set_cell(self, y, x, status):
        self._grid[y][x] = status
    
    #void 
    def iterate_cell(self, grid_copy, idx_y, idx_x):
        alive_surrounds = self._count_alive_surroundings(grid_copy, idx_y, idx_x)

        if grid_copy[idx_y][idx_x] == 0:
            if alive_surrounds == 3:
                self.set_cell(idx_y, idx_x, 1)
        else:
            if alive_surrounds == 2 or alive_surrounds == 3:
                self.set_cell(idx_y, idx_x, 1)
            else:
                self.set_cell(idx_y, idx_x, 0)

    #int
    def _count_alive_surroundings(self, grid_copy, y, x):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue

                self._dy = y + i
                self._dx = x + j
        
                if 0 <= self._dx < self._rows and 0 <= self._dy < self._cols:
                    if grid_copy[self._dy][self._dx] == 1:
                        count += 1

        return count


    #string
    def get_cell(self, idx_y, idx_x):
        return self._grid[idx_y][idx_x]


    def get_grid_copy(self):
        return deepcopy(self._grid)
