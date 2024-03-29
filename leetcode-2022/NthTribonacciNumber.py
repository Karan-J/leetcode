'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
 

Constraints:
0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
'''


def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    a0 = 0
    a1 = 1
    a2 = 1
    x = 0
    for i in range(3,n+1):
        x = a0 + a1 + a2
        a0 = a1
        a1 = a2
        a2 = x 

    return x 


if __name__ == '__main__':
    print(tribonacci(4))
    print(tribonacci(25))