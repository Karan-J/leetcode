'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9

'''

from turtle import width


def searchMatrixSimple(matrix,target):
    for row in matrix:
        if target in row:
            return True
    return False


def searchMatrix(matrix,target):
    if not matrix:
        return False

    for i in range(min(len(matrix),len(matrix[0]))):
        vertical_found = binarySearch(matrix,target,i,True)
        horizontal_found = binarySearch(matrix,target,i,False)
        
        if vertical_found or horizontal_found:
            return True

    return False

def binarySearch(matrix,target,start,is_vertical):
    lo = start
    hi = len(matrix[0]) - 1 if is_vertical else len(matrix) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        if is_vertical:    
            if target < matrix[start][mid]:
                hi = mid - 1
            elif target > matrix[start][mid]:
                lo = mid + 1
            else:
                return True
            
        else:
            if target < matrix[mid][start]:
                hi = mid - 1
            elif target > matrix[mid][start]:
                lo = mid + 1
            else:
                return True
            
    return False


def searchMatrixDC(matrix,target):
    
    if not matrix:
        return False

    def search_rec(left, up, right, down):
        # this submatrix has no height or no width.
        if left > right or up > down:
            return False
        # `target` is already larger than the largest element or smaller
        # than the smallest element in this submatrix.
        elif target < matrix[up][left] or target > matrix[down][right]:
            return False

        mid = left + (right-left) // 2

        # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
        row = up
        while row <= down and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1
        
        return search_rec(left, row, mid - 1, down) or \
                search_rec(mid + 1, up, right, row - 1)

    return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)

    return False

def searchMatrixSSR(matrix,target):
    if not matrix:
        return False
    
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    height = len(matrix)
    width = len(matrix[0])

    row = height - 1
    col = 0

    while col < width and row >= 0:
        if target < matrix[row][col]:
            row -= 1
        elif target > matrix[row][col]:
            col += 1
        else:
            return True

    return False


if __name__ == '__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(searchMatrix(matrix,target),searchMatrixSimple(matrix,target),searchMatrixDC(matrix,target),searchMatrixSSR(matrix,target))
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 20
    print(searchMatrix(matrix,target),searchMatrixSimple(matrix,target),searchMatrixDC(matrix,target),searchMatrixSSR(matrix,target))