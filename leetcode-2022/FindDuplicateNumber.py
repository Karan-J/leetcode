'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

'''


def findDuplicate1(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)

def findDuplicate2(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

def findDuplicate3(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if d[i] == 2:
            return i 


if __name__ == '__main__':
    nums = [1,3,4,2,2]
    print(findDuplicate1(nums),findDuplicate2(nums),findDuplicate3(nums))
    nums = [3,1,3,4,2]
    print(findDuplicate1(nums),findDuplicate2(nums),findDuplicate3(nums))
    nums = [2,4,6,7,8,9,4]
    print(findDuplicate1(nums),findDuplicate2(nums),findDuplicate3(nums))