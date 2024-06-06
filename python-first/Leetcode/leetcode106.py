from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):

        if not inorder or not postorder:
            return None
        
        rootValue = postorder.pop()
        rootNode = TreeNode(rootValue)

        rootIndex = inorder.index(rootValue)

        rootNode.right = self.buildTree(inorder[rootIndex + 1:],postorder)
        rootNode.left = self.buildTree(inorder[:rootIndex],postorder)

        return rootNode
    

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

# Instantiate the Solution class and build the tree
solution = Solution()
root = solution.buildTree(inorder, postorder)

# Function to print the tree in preorder for verification
def print_preorder(node):
    if not node:
        return
    print(node.val, end=' ')
    print_preorder(node.left)
    print_preorder(node.right)

# Print the constructed tree
print_preorder(root)        


        