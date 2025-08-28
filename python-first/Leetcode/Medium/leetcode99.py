# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorder(self, root, vec):
        if root is None:
            return
        self.inorder(root.left, vec)
        vec.append(root.val)
        self.inorder(root.right, vec)
    
    def correctBSTUtil(self, root, vec, index):
        if root is None:
            return index
        index = self.correctBSTUtil(root.left, vec, index)
        root.val = vec[index] 
        index += 1
        index = self.correctBSTUtil(root.right, vec, index)
        return index
    
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        vec = []
        self.inorder(root, vec)
        vec.sort()
        index = 0
        self.correctBSTUtil(root, vec, index)