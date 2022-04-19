'''
You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.

 

Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:
Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.
 

Constraints:
n == nums.length
m == multipliers.length
1 <= m <= 10^3
m <= n <= 10^5
-1000 <= nums[i], multipliers[i] <= 1000
'''


from functools import lru_cache


def maximumScore(nums, multipliers):
    n = len(nums)
    m = len(multipliers)

    @lru_cache(maxsize=2000)
    def dp(i, left):
        if i == m:
            return 0

        mul = multipliers[i]
        right = n - 1 - (i - left)

        return max( mul * nums[left] + dp(i + 1, left + 1), mul * nums[right] + dp(i + 1, left) )

    return dp(0,0)


if __name__ == '__main__':
    nums = [1,2,3]
    multipliers = [3,2,1]
    print(maximumScore(nums,multipliers))
    nums = [-5,-3,-3,-2,7,1]
    multipliers = [-10,-5,3,4,6]
    print(maximumScore(nums,multipliers))
