'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if root is None:
        return True
    if abs( height(root.left) - height(root.right) ) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))

if __name__ == '__main__':
    print(isBalanced(TreeNode(None)))
    t = TreeNode(1)
    l = TreeNode(2)
    r = TreeNode(3)
    t.left = l
    t.right = r
    print(isBalanced(t))
    rr = TreeNode(5)
    rrr = TreeNode(7)
    r.right = rr
    rr.right = rrr
    print(isBalanced(t))
