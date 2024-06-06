# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:

        def preorder(root):
            if not root:
                return ""
            
            # Start with the root value
            resultStr = str(root.val)
            
            # Only add the left part if it exists or if the right part exists (to maintain the correct format)
            if root.left or root.right:
                resultStr += f"({preorder(root.left)})"
            
            # Only add the right part if it exists
            if root.right:
                resultStr += f"({preorder(root.right)})"
            
            return resultStr
        
        return preorder(root)

# Create a sample binary tree
#       1
#      / \
#     2   3
#      \
#       4
root = TreeNode(1)
root.left = TreeNode(2, None, TreeNode(4))
root.right = TreeNode(3)

# Instantiate the Solution class and test the tree2str function
solution = Solution()
tree_str = solution.tree2str(root)
print(tree_str)
