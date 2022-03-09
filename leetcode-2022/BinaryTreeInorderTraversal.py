'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

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

    def inorderTraversal(self,root):
        res = []
        self.inorder(root,res)
        return res

    def inorder(self,root,res):
        if not root:
            return
        else:
            self.inorder(root.left,res)
            res.append(root.val)
            # print(root.val)
            self.inorder(root.right,res)


if __name__ == '__main__':
    root = []
    s = Solution()
    print(s.inorderTraversal(root))
    root = TreeNode(1)
    print(s.inorderTraversal(root))
    r = TreeNode(2)
    l = TreeNode(3)
    root.right = r
    root.left = None
    r.left = l 
    print(s.inorderTraversal(root))
