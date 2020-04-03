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

# print_board()

def check_row(row, num):
    for i in range(9):
        if board[row][i]==num:
            return False
    return True

def check_column(row, col):
    for i in range(9):
        if board[i][col]==num:
            return False
    return True

def check_box(row, col):
    for i in range(3):
        for j in range(3):
            if board[i+row][(j+col)%3]==num:
                return False
    return True


print(check_row(0, 1))

# while True:
#     for nums in board:
#         for num in nums:
#             if num==0:
