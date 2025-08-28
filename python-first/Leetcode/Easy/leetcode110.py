# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):

        def checkHeight(node):

            if not node:
                return 0
            
            lh = checkHeight(node.left)
            rh = checkHeight(node.right)

            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1+max(lh,rh)
        return checkHeight(root) != -1
        