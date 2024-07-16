
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left = None
        self.right = right = None

class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        # Find the root of the left subtree, which is preorder[1]
        left_subtree_root_val = preorder[1]
        # Find the index of the left subtree root in the postorder array
        left_subtree_root_index = postorder.index(left_subtree_root_val)

        # Split the preorder and postorder arrays into left and right subtrees
        # Left subtree
        left_preorder = preorder[1:left_subtree_root_index + 2]
        left_postorder = postorder[:left_subtree_root_index + 1]

        # Right subtree
        right_preorder = preorder[left_subtree_root_index + 2:]
        right_postorder = postorder[left_subtree_root_index + 1:-1]

        # Recursively construct the left and right subtrees
        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root

# Example usage
# Preorder and postorder arrays
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

# Instantiate the Solution class and build the tree
solution = Solution()
root = solution.constructFromPrePost(preorder, postorder)

# Function to print the tree in preorder for verification
def print_preorder(node):
    if not node:
        return
    print(node.val, end=' ')
    print_preorder(node.left)
    print_preorder(node.right)

# Print the constructed tree
print_preorder(root)
