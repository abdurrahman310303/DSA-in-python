# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage
# Create tree nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(1)
node4 = TreeNode(2)

# Link nodes together to form trees
node1.right = node2
node3.right = node4

# Create an instance of the Solution class
sol = Solution()

# Check if trees are the same
print(sol.isSameTree(node1, node3))  # Output: True
