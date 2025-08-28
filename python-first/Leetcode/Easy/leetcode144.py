# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):

        result = []
        self.preOrderhelper(root,result)

        return result
    
    def preOrderhelper(self,root,result) :

        if root:
            result.append(root.val)
            self.preOrderhelper(root.left,result)
            self.preOrderhelper(root.right,result)
        