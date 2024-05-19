class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.left is None:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    res = search(root.left, key)
    if res:
        return res
    return search(root.right, key)

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = minValueNode(root.right)
        root.right = delete(root.right, root.val)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root:
        print(root.val, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val, end=" ")

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False

# Example usage
root = None
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)

print("Inorder traversal:")
inorderTraversal(root)
print("\nPreorder traversal:")
preorderTraversal(root)
print("\nPostorder traversal:")
postorderTraversal(root)

key = 6
print(f"\n\nSearch for {key}: {'Found' if search(root, key) else 'Not found'}")

key = 3
root = delete(root, key)
print(f"\nAfter deleting {key}:")
inorderTraversal(root)

print("\n\nHeight of tree:", height(root))
print("Number of nodes in tree:", countNodes(root))
print("Is tree balanced?", "Yes" if isBalanced(root) else "No")
