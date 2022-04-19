'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

'''

def maximalSquare(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sq_len = 0
    dp = [ [0] * (cols + 1) for i in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min( dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] ) + 1
                max_sq_len = max( dp[i][j], max_sq_len )

    return max_sq_len ** 2

if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximalSquare(matrix))
    matrix = [["0","1"],["1","0"]]
    print(maximalSquare(matrix))
    matrix = [["0"]]
    print(maximalSquare(matrix))