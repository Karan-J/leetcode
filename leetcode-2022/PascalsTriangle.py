

def generatePascalsTriangle(numRows):
    triangle = []

    for row_num in range(numRows):

        row = [None for _ in range(row_num + 1)]
        row[0] = 1
        row[-1] = 1

        for j in range(1,len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)

    return triangle


def myGeneratePascalsTriangle(numRows):
    ans = []
    # if numRows == 1:
    #     return [[1]]
    # elif numRows == 2:
    #     return [[1],[1,1]]
    
    for i in range(numRows):
        temp = []
        c = 0
        for j in range(i+1):
            if j == 0:
                temp.append(1)
            elif j == i:
                temp.append(1)
            else:
                prevRow = ans[i-1]
                temp.append(sum(prevRow[c:c+2]))
                c += 1
        ans.append(temp)
    
    return ans

def generatePascalSimple(numRows):
    if numRows   == 0: 
        return []
    elif numRows == 1: 
        return [[1]]
    Tri = [[1]]
    for i in range(1,numRows):
        row = [1]
        for j in range(1,i):
            row.append(Tri[i-1][j-1] + Tri[i-1][j]) 
        row.append(1)
        Tri.append(row)
    return Tri

if __name__ == '__main__':
    print(generatePascalsTriangle(numRows=1))
    print(myGeneratePascalsTriangle(numRows=1))
    print(generatePascalsTriangle(numRows=3))
    print(myGeneratePascalsTriangle(numRows=3))
    print(generatePascalsTriangle(numRows=5))
    print(myGeneratePascalsTriangle(numRows=5))
    print(generatePascalSimple(5))
    print(generatePascalsTriangle(numRows=7))
    print(myGeneratePascalsTriangle(numRows=7))
    print(myGeneratePascalsTriangle(numRows=4))