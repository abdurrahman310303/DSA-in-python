# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root):
        result = []
        self.postOrderHelper(root,result)

        return result

    def postOrderHelper(self,root,result):

        if root:
            self.postOrderHelper(root.left,result)
            self.postOrderHelper(root.right,result)
            result.append(root.val)        