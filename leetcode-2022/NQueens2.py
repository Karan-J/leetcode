'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.


Example 2:
Input: n = 1
Output: 1
 

Constraints:
1 <= n <= 9

'''


def totalNQueens(number_of_queens):

    def backtrack(row,columns,diagonals,anti_diagonals):

        if row == number_of_queens:
            return 1

        solutions = 0

        for col in range(number_of_queens):
            curr_diagonal = row - col
            curr_anti_diagonal = row + col

            if col in columns or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                continue

            columns.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)

            solutions += backtrack(row+1, columns, diagonals, anti_diagonals)

            columns.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)

        return solutions

    return backtrack(0,set(),set(),set())


if __name__ == '__main__':
    number_of_queens = 4
    print(totalNQueens(number_of_queens))
    number_of_queens = 1
    print(totalNQueens(number_of_queens))
    number_of_queens = 8
    print(totalNQueens(number_of_queens))