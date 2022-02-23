'''
Given an m x n matrix, return all elements of the matrix in spiral order.
 

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

def spiralOrder(matrix):
    if matrix is None or matrix[0] is None:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    up = left = 0
    down = rows - 1
    right = cols - 1

    ans = []

    while len(ans) < rows * cols:

        # go left
        for col in range(left,right + 1):
            ans.append(matrix[up][col])

        # go down
        for row in range(up + 1, down + 1):
            ans.append(matrix[row][right])

        if up != down:
            for col in range(right - 1, left - 1, -1):
                ans.append(matrix[down][col])

        if left != right:
            for row in range(down - 1, up, -1):
                ans.append(matrix[row][left])

        up += 1
        left += 1
        right -= 1
        down -= 1

    return ans


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))