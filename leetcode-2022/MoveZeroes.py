'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

def moveZeroes(nums):
    l = len(nums)
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
        j += 1
    while i < len(nums):
        nums[i] = 0
        i += 1
    # print(nums)
    return nums


def moveZeroesOnePass(nums):
    l = len(nums)
    i = 0
    for j in range(l):
        if nums[j] != 0 and nums[i] == 0:
            nums[i],nums[j] = nums[j],nums[i]
        # print(nums)
        if nums[i] != 0:
            i += 1
    return nums


if __name__ == '__main__':
    nums = [0,1,0,3,12]
    print(moveZeroes(nums))
    nums = [0,1,0,3,12]
    print(moveZeroesOnePass(nums))
    nums = [0]
    print(moveZeroes(nums)) 
    nums = [0]
    print(moveZeroesOnePass(nums))
    nums = [1,5,0,2,0,0,3,0,0,1,8,0,4,6]
    print(moveZeroes(nums))
    nums = [1,5,0,2,0,0,3,0,0,1,8,0,4,6]
    print(moveZeroesOnePass(nums))