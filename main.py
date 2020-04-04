def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=' ')
        print()

def check_empty(board, loc):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                loc[0]=row
                loc[1]=col
                return True
    return False

def check_row(board, row, num):
    for i in range(9):
        if board[row][i]==num:
            return False
    return True

def check_column(board, col, num):
    for i in range(9):
        if board[i][col]==num:
            return False
    return True

def check_box(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i+(row-row%3)][j+(col-col%3)]==num:
                return False
    return True

def check_all(board, row, col, num):
    return check_row(board, row, num) and check_column(board, col, num) and check_box(board, row, col, num)


def solve(board):

    loc = [0, 0]

    if not check_empty(board, loc):
        return True

    row, col = loc[0], loc[1]

    for num in range(1, 10):
        if check_all(board, row, col, num):
            board[row][col]=num
            if solve(board):
                return True
            board[row][col]=0
    return False

######################
#        GUI         #
######################


import pygame
from solver import solve, check_all
import time
pygame.font.init()


class Grid:
    # To change the starting board change this
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, row, col, val):
        # if self.cubes[row][col].value == 0:
        self.cubes[row][col].set(val)
        self.update_model()

            # if not(check_all(self.model, row,col, val)) and solve(self.model):
            #     return True
            # else:
            #     self.cubes[row][col].set(0)
            #     self.cubes[row][col].set_temp(0)
            #     self.update_model()
            #     return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    # def clear(self):
    #     row, col = self.selected
    #     if self.cubes[row][col].value == 0:
    #         self.cubes[row][col].set_temp(0)

    def click(self, pos):
        """
        :param: pos
        :return: (row, col)
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y),int(x))
        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width ,height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y, gap ,gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board):
    win.fill((255,255,255))
    board.draw(win)


def main():
    win = pygame.display.set_mode((540,600))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_SPACE:
                    if board.is_finished():
                        print("SUCCESS")
                    key = None

        redraw_window(win, board)
        pygame.display.update()


main()
pygame.quit()
