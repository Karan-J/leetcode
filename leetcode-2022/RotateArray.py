'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

'''

def rotateArray(nums,k):
    n = len(nums)
    k = k % n

    li = [0] * n 
    for i in range(len(nums)):
        li[ (i + k) % n ] = nums[i]

    nums[:] = li
    return nums 


def rotateArrayConstantSpace(nums,k):
    n = len(nums)
    k = k % n
    # nums = reverse(nums, 0, n - 1)
    reverse(nums, 0, n - 1)
    # nums = reverse(nums, 0, k - 1)
    reverse(nums, 0, k - 1)
    # nums = reverse(nums, k, n - 1)
    reverse(nums, k, n - 1)
    # print(nums)
    return nums
    

def reverse(nums,start,end):
    while start < end:
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1
    # print(nums)
    # return nums


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(nums,k)
    print(rotateArray(nums,k))
    # print(rotateArrayConstantSpace(nums,k))
    nums = [-1,-100,3,99]
    k = 2    
    print(nums,k)
    print(rotateArray(nums,k))
    # print(rotateArrayConstantSpace(nums,k))
    