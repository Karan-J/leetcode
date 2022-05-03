'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
 
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''

# Dynamic Programming version
import math


def maxSubArray(arr):
    curr_sum = max_sum = arr[0]

    for i in range(1,len(arr)):
        num = arr[i]
        curr_sum = max(num,curr_sum + num)
        max_sum = max(curr_sum,max_sum)

    return max_sum

# Divide and conquer version
def maxSubArrayDc(arr):
    return maxSub(arr,0,len(arr) - 1)

def maxSub(arr,left,right):
    if left > right:
        return -math.inf
    mid = (left + right) // 2

    curr = lsum = rsum = 0
    for i in range(mid-1,left-1,-1):
        curr += arr[i]
        lsum = max(lsum,curr)

    curr = 0
    for i in range(mid+1,right+1):
        curr += arr[i]
        rsum = max(rsum,curr)

    best_sum = lsum + arr[mid] + rsum

    L = maxSub(arr, left, mid - 1)
    R = maxSub(arr, mid + 1, right)
    return max(L,R,best_sum)


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums),maxSubArrayDc(nums))
    nums = [1]
    print(maxSubArray(nums),maxSubArrayDc(nums))
    nums =[5,4,-1,7,8]
    print(maxSubArray(nums),maxSubArrayDc(nums))
    nums = [i for i in range(-10,1)]
    print(maxSubArray(nums),maxSubArrayDc(nums))
    nums = [2,3,3,4]
    print(maxSubArray(nums),maxSubArrayDc(nums))