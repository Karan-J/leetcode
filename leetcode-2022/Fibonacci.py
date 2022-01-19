'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''


def fib( n: int) -> int:
    if n < 2:
        return n
        
    first = 0
    second = 1

    for i in range(2,n+1):
        third = first + second
        first = second
        second = third
        
    return second

if __name__ == '__main__':
    for i in range(8):
        print(i,'->',fib(i))
	# print(fib(2))       # ans = 1
    # print(fib(3))       # ans = 2 
    # print(fib(4))       # ans = 3
