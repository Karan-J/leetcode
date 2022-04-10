'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
'''

def linearFindMedian(nums1, nums2):         #O(m+n)
    i = 0
    j = 0
    m = len(nums1)
    n = len(nums2)
    merged = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        elif nums1[i] >= nums2[j]:
            merged.append(nums2[j])
            j += 1

    while i <= m - 1:
        merged.append(nums1[i])
        i += 1

    while j <= n - 1:
        merged.append(nums2[j])
        j += 1

    print(merged)
    if (m + n) % 2 == 1:
        return merged[(m + n)//2]
    else:
        return ( merged[(m + n)//2 - 1] + merged[(m + n)//2] ) / 2


def logFindMedian(nums1, nums2):    #O(log(m+n))
    l = len(nums1) + len(nums2)

    def kth(nums1,nums2, k):
        if len(nums1) == 0:
            return nums2[k]
        elif len(nums2) == 0:
            return nums1[k]
        ia = len(nums1) // 2
        ib = len(nums2) // 2
        ma = nums1[ia]
        mb = nums2[ib]

        if (ia + ib) < k:   #k is greater, go right
            if ma > mb:     # discard b's lower half
                return kth(nums1, nums2[ib + 1:], k - ib - 1)
            else:           #discard a's lower half
                return kth(nums1[ia + 1:], nums2, k - ia - 1)
        else:
            if ma > mb:     # discard a's upper half
                return kth(nums1[:ia], nums2, k)
            else:           # discard b's upper half
                return kth(nums1, nums2[:ib], k)

    if l % 2 == 0:
        return (kth(nums1, nums2, l//2 - 1 ) + kth(nums1, nums2, l//2 ) ) / 2
    else:
        return kth(nums1, nums2, l//2)


if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    print(linearFindMedian(nums1,nums2), logFindMedian(nums1,nums2))
    nums2 = [2,4]
    print(linearFindMedian(nums1,nums2), logFindMedian(nums1,nums2))