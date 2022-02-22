'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5
'''

def findDiagonalOrder(mat):
    if mat is None or mat[0] is None:
        return []

    rows = len(mat)
    cols = len(mat[0])

    ans = []
    temp = []

    for diag in range(rows + cols - 1):

        temp.clear()

        r = 0 if diag < cols else diag - cols + 1
        c = diag if diag < cols else cols - 1

        while r < rows and c > -1:
            temp.append(mat[r][c])
            r += 1
            c -= 1

        if diag % 2 == 0:
            ans.extend(temp[::-1])
        else:
            ans.extend(temp)

    return ans

if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(findDiagonalOrder(mat))
    mat = [[1,2],[3,4]]
    print(findDiagonalOrder(mat))
    mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
    print(findDiagonalOrder(mat))