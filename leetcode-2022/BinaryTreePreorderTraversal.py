'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTraversal(self,root):
        res = []
        self.preorder(root,res)
        return res

    def preorder(self,root,res):
        if not root:
            return res
        else:
            res.append(root.val)
            self.preorder(root.left,res)
            # print(root.val)
            self.preorder(root.right,res)


if __name__ == '__main__':
    root = []
    s = Solution()
    print(s.preorderTraversal(root))
    root = TreeNode(1)
    print(s.preorderTraversal(root))
    r = TreeNode(2)
    l = TreeNode(3)
    root.right = r
    root.left = None
    r.left = l 
    print(s.preorderTraversal(root))
