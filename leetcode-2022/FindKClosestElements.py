'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
'''


def findClosestElements(arr,k,x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = left + (right - left) // 2
        if x < arr[mid]:
            right = mid
        elif x > arr[mid + k]:
            left = mid + 1
        elif abs(arr[mid] - x) <= abs(arr[mid + k] - x):
            right = mid
        else:
            left = mid + 1

    return arr[left:left + k]


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    print(findClosestElements(arr,k,x))
    k = 2
    x = -1
    print(findClosestElements(arr,k,x))