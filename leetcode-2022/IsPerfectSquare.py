'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
 

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
 

Constraints:
1 <= num <= 2^31 - 1
'''

def isPerfectSquare(num):
    left = 0
    right = num

    while left <= right:
        mid = left + (right - left) // 2
        x = mid * mid 
        if x == num:
            return True
        elif num < x:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    print(isPerfectSquare(16))
    print(isPerfectSquare(14))
    print(isPerfectSquare(100))