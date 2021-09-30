class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        y = [0,0]
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(len(nums)):
                if diff == nums[j]:
                    y[0] = i
                    y[1] = j
                    break
        return y
        

