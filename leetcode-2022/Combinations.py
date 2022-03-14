'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 
Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
 

Constraints:
1 <= n <= 20
1 <= k <= n

'''

import itertools 

def combineFast(n,k):
    return [i for i in itertools.combinations([i for i in range(1,n+1)],k)]

def combine(n,k):

    def backtrack(first = 1, curr = []):
        if len(curr) == k:
            output.append(curr[:])

        for i in range(first,n+1):
            curr.append(i)
            backtrack(i+1,curr)
            curr.pop()

    output = []
    backtrack()
    return output

if __name__ == '__main__':
    print(combine(4,2),combineFast(4,2))
    print(combine(1,1),combineFast(1,1))
    print(combine(4,3),combineFast(4,3))