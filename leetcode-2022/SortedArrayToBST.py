'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
 

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.
'''
from BalancedBinaryTree import isBalanced

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    return helper(0,len(nums) - 1,nums)

def helper(left,right,nums):
    if left > right:
        return None
    
    mid = (left + right) // 2

    root = TreeNode(nums[mid])
    root.left = helper(left, mid - 1,nums)
    root.right = helper(mid + 1,right,nums)
    return root

def preorder(root):
    if root is None:
        return None
    print(root.val)
    preorder(root.left)
    preorder(root.right)

if __name__ == '__main__':
    nums = [i for i in range(10)]
    t = sortedArrayToBST(nums)
    # print(t)
    preorder(t)
    print('isBalanced =', isBalanced(t))
    print('Another tree')
    n = [-10,-3,0,5,9]
    tt = sortedArrayToBST(n)
    preorder(tt)