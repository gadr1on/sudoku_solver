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

if __name__ == "__main__":

    board = [[5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]]

    if solve(board):
        print_board(board)
    else:
        print('No solution exists')
