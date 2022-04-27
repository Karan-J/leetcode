'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

'''

def lis(nums):
    dp = [1] * len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max( dp[i], dp[j] + 1 )
    return max(dp)


def lengthOfLIS(nums):
    sub = [nums[0]]

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            i = 0
            while i < len(sub):
                if sub[i] > num:
                    sub[i] = num
                i += 1
    
    return len(sub)

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(lis(nums), lengthOfLIS(nums))
    nums = [0,1,0,3,2,3]
    print(lis(nums), lengthOfLIS(nums))
    nums = [7,7,7,7,7,7,7]
    print(lis(nums), lengthOfLIS(nums))
    nums = [2,4,5,7,2,9,6,5,10,43,21,36,78]
    print(lis(nums), lengthOfLIS(nums))