# nums = [0,1,2,2,3,0,4,2]
# val = 2
# nums = sorted(nums)
# for i in range(len(nums)):
#     print(i,nums)
#     if nums[i]==val:
#         del nums[i]

print('22222222222222222222222222222222222222222')

nums = [0,1,2,2,3,0,4,2]
val = 2
nums = sorted(nums)
print(nums)
# for i in nums:
#     if val==i:
#         nums.remove(val)
#
#     print(nums)
ind = []
le = len(nums)
for i in range(len(nums)):
    if nums[i]==val:
        ind.append(i)
        # nums.pop(i)

print(ind)

for i in ind:
    nums.remove(nums[i])

print(nums)



nums = [0,1,2,2,3,0,4,2]
print(nums,"````````````````")

while val in nums:
    print(nums)
    nums.remove(val)

print(nums)

nums = [3,2,2,3]