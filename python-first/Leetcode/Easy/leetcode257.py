from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, result):
            if node:
                # Append the current node value to the path
                path.append(str(node.val))
                
                # If it's a leaf node, append the path to the result
                if not node.left and not node.right:
                    result.append("->".join(path))
                else:
                    # Continue the DFS on left and right children
                    dfs(node.left, path, result)
                    dfs(node.right, path, result)
                
                # Backtrack to explore other paths
                path.pop()
        
        result = []
        dfs(root, [], result)
        return result

# Example usage
# Creating a binary tree: 
#     1
#    / \
#   2   3
#    \
#     5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = Solution()
print(solution.binaryTreePaths(root))  # Output: ["1->2->5", "1->3"]
