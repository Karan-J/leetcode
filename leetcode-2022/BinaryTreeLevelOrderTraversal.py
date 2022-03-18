'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    if root is None:
        return []
    tree = []
    level = 0
    qu = deque([root,])

    while qu:
        temp = []
        level_length = len(qu)
        tree.append(temp)

        for i in range(level_length):
            node = qu.popleft()
            tree[level].append(node.val)
            
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)

        level += 1

    # print(tree)
    return tree



if __name__ == '__main__':
    root = None
    print(levelOrderTraversal(root))
    root = TreeNode(val = 1)
    print(levelOrderTraversal(root))
    l = TreeNode(val = 3)
    r = TreeNode(val = 15)
    root.left = l
    root.right = r
    r.left = TreeNode(val = 17)
    r.right = TreeNode(val = 20)
    print(levelOrderTraversal(root))