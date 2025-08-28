# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []
        self.inOrder(root,result)

        return result

    def inOrder(self,root,result):
        if root:
            self.inOrder(root.left,result)
            result.append(root.val)

            self.inOrder(root.right,result)
        