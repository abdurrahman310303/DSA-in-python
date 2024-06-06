from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is the root
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder list
        root_index = inorder.index(root_val)
        
        # Recursively construct the left and right subtrees
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        
        return root

# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
solution = Solution()
root = solution.buildTree(preorder, inorder)

# Helper function to print the tree (in-order traversal for testing)
def inorder_traversal(root: Optional[TreeNode]):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

print(inorder_traversal(root))  # Output: [9, 3, 15, 20, 7]
