'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

def permute(nums):
    
    def backtrack(first = 0):
        if first == n:
            out.append(nums[:])

        for i in range(first,n):
            nums[first],nums[i] = nums[i],nums[first]
            backtrack(first + 1)
            nums[first],nums[i] = nums[i],nums[first]
            

    out = []
    n = len(nums)
    backtrack()
    return out


if __name__ == '__main__':
    nums = [1]
    print(permute(nums))
    nums = [1,2]
    print(permute(nums))
    nums = [1,2,3]
    print(permute(nums))
    nums = [1,2,3,4]
    print(permute(nums))