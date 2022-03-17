'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
'''

# brute-force
def generateParen(n):

    def generate(A = []):
        if len(A) == 2*n:
            if isValid(A):
                ans.append(''.join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def isValid(A):
        bal = 0
        for i in A:
            if i == '(':
                bal += 1
            elif i == ')':
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    ans = []
    generate()
    return ans

# backtracking approach
def generateParentheses(n):
    def backtrack(S = [],left = 0, right = 0):
        if len(S) == 2*n:
            ans.append(''.join(S))
            return ans
        if left < n:
            S.append('(')
            backtrack(S,left + 1, right)
            S.pop()
        if right < left:
            S.append(')')
            backtrack(S,left,right + 1)
            S.pop()

    ans = []
    backtrack()
    return ans


def generateP(n):
    ans = []
    if n == 0:
        return ['']
    for i in range(n):
        for left in generateP(i):
            for right in generateP(n - 1 - i):
                ans.append('({}){}'.format(left,right))
    return ans


if __name__ == '__main__':
    print(generateParentheses(3),generateParen(3),generateP(3))
    print(generateParentheses(2),generateParen(2),generateP(2))
    print(generateParentheses(1),generateParen(1),generateP(1))
