# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        if not root:
            return True
        
        sort_check = []
        self.inorder(root,sort_check)

        for i in range(1,len(sort_check)):

            if sort_check[i-1] >= sort_check[i]:
                return False
        return True

    def inorder(self,root,sort_check):

        if root:

            self.inorder(root.left,sort_check)
            sort_check.append(root.val)
            self.inorder(root.right,sort_check)




        