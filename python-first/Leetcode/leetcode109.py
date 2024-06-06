from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Step 1: Convert Linked List to Array
        def mapListToValues(head: ListNode) -> List[int]:
            values = []
            while head:
                values.append(head.val)
                head = head.next
            return values
        
        # Step 2: Convert Array to Height-Balanced BST
        def sortedArrayToBST(values: List[int]) -> Optional[TreeNode]:
            if not values:
                return None
            
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = sortedArrayToBST(values[:mid])
            root.right = sortedArrayToBST(values[mid + 1:])
            return root
        
        values = mapListToValues(head)
        return sortedArrayToBST(values)

# Helper function to print the tree in-order (for testing purposes)
def in_order_traversal(root: Optional[TreeNode]):
    return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right) if root else []

# Example usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Converting to BST
solution = Solution()
bst_root = solution.sortedListToBST(head)

# Printing the in-order traversal of the BST (should be sorted order)
print(in_order_traversal(bst_root))  # Output: [1, 2, 3, 4, 5]
