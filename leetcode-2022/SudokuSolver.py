'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:



Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
'''

from collections import defaultdict



def solveSudoku(board):

    def boxIndex(row,col):
        return (row//n) * n + col//n


    def couldPlace(d,row,col):
        return not ((d in rows[row]) or (d in cols[col]) or (d in boxes[boxIndex(row,col)]) )


    def placeNumber(d,row,col):
        rows[row][d] += 1
        cols[col][d] += 1
        boxes[boxIndex(row,col)][d] += 1
        board[row][col] = str(d)


    def removeNumber(d,row,col):
        del rows[row][d] 
        del cols[col][d]
        del boxes[boxIndex(row,col)][d]
        board[row][col] = '.'


    def placeNextNumbers(row,col):
        if row == N - 1 and col == N - 1:
            nonlocal sudokuSolved
            sudokuSolved = True
        else:
            if col == N - 1:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)
        

    def backtrack(row = 0, col = 0):
        if board[row][col] == '.':
            for d in range(1,N + 1):
                if couldPlace(d,row,col):
                    placeNumber(d,row,col)
                    placeNextNumbers(row,col)

                    if not sudokuSolved:
                        removeNumber(d,row,col)
        else:
            placeNextNumbers(row,col)


    n = 3
    N = n * n 

    rows = [defaultdict(int) for i in range(N)]
    cols = [defaultdict(int) for i in range(N)]
    boxes = [defaultdict(int) for i in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] != '.':
                d = int(board[i][j])
                placeNumber(d,i,j)

    sudokuSolved = False
    backtrack()
    return board


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(solveSudoku(board))