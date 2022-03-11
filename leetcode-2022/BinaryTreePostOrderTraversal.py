'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

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


def postOrderTraversal(root):
    res = []
    postOrder(root,res)
    return res 

def postOrder(root,res):
    if not root:
        return res
    postOrder(root.left,res)
    postOrder(root.right,res)
    res.append(root.val)


if __name__ == '__main__':
    root = []
    print(postOrderTraversal(root))
    root = TreeNode(1)
    print(postOrderTraversal(root))
    r = TreeNode(2)
    l = TreeNode(3)
    root.right = r
    root.left = None
    r.left = l 
    print(postOrderTraversal(root))