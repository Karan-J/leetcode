'''
Given an array of integers nums, sort the array in ascending order.

 

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:
1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
'''

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left,right)

def merge(left,right):
    l = 0
    r = 0
    nums = []

    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            nums.append(left[l])
            l += 1

        else:
            nums.append(right[r])
            r += 1

    while l < len(left):
        nums.append(left[l])
        l += 1

    while r < len(right):
        nums.append(right[r])
        r += 1

    return nums


if __name__ == '__main__':
    nums = [-2,4,-2,1,0,4,9,3,99,-100]
    print(mergeSort(nums))
    nums = [5,2,3,1]
    print(mergeSort(nums))
    nums = [5,1,1,2,0,0]
    print(mergeSort(nums))
    nums = [2,4,67,8,3,12,8,7,3,6]
    print(mergeSort(nums))