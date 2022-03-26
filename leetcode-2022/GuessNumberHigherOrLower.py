'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 
Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
'''

def guessNumber(n,pick):
    low = 0
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        g = pick - mid
        # print(g)
        if g == 0:
            return mid
        elif g >= 1:
            low = mid + 1
        elif g <= -1:
            high = mid - 1


if __name__ == '__main__':
    print(guessNumber(300,29))
    print(guessNumber(100000, 89))
    