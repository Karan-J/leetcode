'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9

'''

# def searchRange(nums, target):
        
#     lower_bound = findBound(nums, target, True)
#     if (lower_bound == -1):
#         return [-1, -1]
    
#     upper_bound = findBound(nums, target, False)
#     return [lower_bound, upper_bound]
        


# def findBound(nums, target, isFirst):
    
#     N = len(nums)
#     begin = 0 
#     end = N - 1
#     while begin <= end:
#         mid = end - (begin + end) // 2   
        
#         if nums[mid] == target:
            
#             if isFirst:
#                 # This means we found our lower bound.
#                 if mid == begin or nums[mid - 1] < target:
#                     return mid

#                 # Search on the left side for the bound.
#                 end = mid - 1
                
#             else:
                
#                 # This means we found our upper bound.
#                 if mid == end or nums[mid + 1] > target:
#                     return mid
                
#                 # Search on the right side for the bound.
#                 begin = mid + 1
        
#         elif nums[mid] > target:
#             end = mid - 1
#         else:
#             begin = mid + 1
    
#     return -1


def search(nums, target):
    out = []
    left = 0
    right = len(nums) - 1
    if len(nums) == 0:
        return [-1,-1]
    
    def searchLow(nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def searchHigh(nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right
    
    low = (searchLow(nums,target))
    high = (searchHigh(nums,target))
    # print(low,high)
    if low in range(0,right + 1) and low <= high and nums[low] == target:
        return [low,high]
    
    else:
        return [-1,-1]
            


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    print(search(nums,target))
    # print(searchRange(nums,target))
    
    target = 6
    # print(searchRange(nums,target))
    print(search(nums,target))
    nums = []
    target = 0
    # print(searchRange(nums,target))
    print(search(nums,target))
