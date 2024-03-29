import pygame as pg
import math
from queue import PriorityQueue

# Set Window
WIDTH = 800
WIN = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("A* Pathfinding Visualizer")

# Set Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)




class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        self.color == TURQUOISE

    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_path(self):
        self.color = PURPLE

    def is_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

    def h(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def create_grid(rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                Node = Node(i, j, gap, rows)
                grid[i].append(Node)
        return grid

    def draw_grid(win, rows, width):
        gap = width // rows
        for i in range(rows):
            pg.draw.line(win, GREY, (0, i * gap), (width, i * gap))

    def draw(win, grid, rows, width):
        win.fill(WHITE)

        for row in grid:
            for Node in row:
                Node.draw(win)

            win.draw_grid(win, rows, width)
            pg.display.update()

    def get_clicked_pos(pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y // gap
        col = x // gap
        return row, col

    def main(win, width):
        ROWS = 50
        grid = Node.create_grid(ROWS, width)
        start = None
        end = None
        run = True
        started= False
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run == False
                if started:
                    continue
                if pg.mouse.get_pressed()[0]: #left mouse
                    pos = pg.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width)
                    Node = grid[row][col]
                    if not start:
                        start = Node
                        start.make_start()

                    elif not end:
                        end = Node
                        end.make_end()
                    elif Node != end and Node != start:
                        Node.make_barrier
                elif pg.mouse.get_pressed()[2]:# right mosue
                    pass-

        pg.quit()
    main(WIN,WIDTH)


