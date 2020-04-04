board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]



def print_board():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


def check_empty(arr, loc):
    for row in range(9):
        for col in range(9):
            if arr[row][col]==0:
                loc[0]=row
                loc[1]=col
                return True
    return False

def check_row(arr, row, num):
    for i in range(9):
        if arr[row][i]==num:
            return False
    return True

def check_column(arr, col, num):
    for i in range(9):
        if arr[i][col]==num:
            return False
    return True

def check_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i+(row-row%3)][j+(col-col%3)]==num:
                return False
    return True

def check_all(arr, row, col, num):
    return check_row(arr, row, num) and check_column(arr, col, num) and check_box(arr, row, col, num)


def solve(arr):

    loc = [0, 0]

    if not check_empty(arr, loc):
        return True

    row, col = loc[0], loc[1]

    for num in range(9):
        if check_all(arr, row, col, num+1):
            arr[row][col]=num+1

            if solve(arr):
                return True

            arr[row][col]=0
    return False

solve(board)

# def hello():
#     board[0][2]=1
#
# hello()
print_board()

# def test():
#     for i in range(1,10):
#         print(f'{i} -> {check_box(0, 2, i)}')
#
# test()
