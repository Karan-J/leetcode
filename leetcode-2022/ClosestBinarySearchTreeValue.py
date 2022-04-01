'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
 

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^9
-10^9 <= target <= 10^9
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closestValue(root,target):
    if root.left is None and root.right is None:
        return root.val
    
    closest = root.val
    while root:
        closest = min(root.val, closest, key = lambda x: abs(target - x))
        root = root.left if target < root.val else root.right
    return closest


if __name__ == '__main__':
    root = TreeNode(4)
    l = TreeNode(2)
    r = TreeNode(5)
    ll = TreeNode(1)
    lr = TreeNode(3)
    root.left = l
    root.right = r
    l.left = ll
    l.right = lr

    print(closestValue(root,target=3.72412))
    print(closestValue(root, target= 3.12132))
    root = TreeNode(4)
    print(closestValue(root,target=1.123214))