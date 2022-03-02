'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
 

Constraints:
0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]
    ans = []
    ans.append([1])
    for i in range(1,rowIndex + 1):
        temp = [0] * (i+1)
        temp[0] = 1
        temp[-1] = 1
        prev = ans[i-1]

        for j in range(1,i):
            x = prev[j]
            y = prev[j-1]
            temp[j] = x + y
        
        ans.append(temp)
    return ans[rowIndex]

if __name__ == '__main__':
    print(0,getRow(0))
    print(1,getRow(1))
    print(3,getRow(3))
    print(9,getRow(9))
    print(10,getRow(10))
