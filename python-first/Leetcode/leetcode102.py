from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            temp = queue.popleft()
            current_level.append(temp.val)
            
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        
        result.append(current_level)
    
    return result
