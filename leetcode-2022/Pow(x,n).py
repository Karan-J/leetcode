'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25 

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''


def myPow(x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        return fastPow(x,n)
    
def fastPow(x,n):
    if n == 0:
        return 1
    halfPow = fastPow(x,n//2)
    if n % 2 == 0:
        return halfPow * halfPow
    else:
        return x * halfPow * halfPow

if __name__ == '__main__':
    x = 2
    for i in range(-3,5):
        print(i,'->',myPow(x,i))

'''
Approach 1: Brute Force
Approach 2: Fast Power Algorithm Recursive
Approach 3: Fast Power Algorithm Iterative
'''