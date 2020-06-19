def removeDuplicates(nums):
    l = len(nums)
    i = 0
    while i < len(nums) - 1:
        # print(nums[i], nums[i + 1],i,i+1)
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    print(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)

# nums = [0,0,1,1,1,2,2,3,3,4]
#
# f = 0
# set = {}
# for i in nums:
#     pass
#     # set.add(i)
#     # print(nums, set)
#
# # l = list(s)
# print(type({2,4,5}))