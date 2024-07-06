from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root,key):

    newNode = Node(key)

    if root is None:
        return newNode
    
    queue = deque([root])

    while queue:

        temp = queue.popleft()

        if not temp.left:
            temp.left = newNode
            break
        else:
            queue.append(temp.left)
        
        if not temp.right:
            temp.right = newNode
            break
        else:
            queue.append(temp.right)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    res = search(root.left, key)
    if res:
        return res
    return search(root.right, key)

def findMin(root):
    if root is None:
        return float('inf')
    
    res = root.val
    lres = findMin(root.left)
    rres = findMin(root.right)

    if lres < res:
        res = lres
    
    if rres < res:
        res = rres

    return res

def findMax(root):
    if root is None:
        return float('-inf')
    res = root.val
    lres = findMax(root.left)
    rres = findMax(root.right)

    if lres > res:
        res = lres
    if rres > res:
        res = rres
    
    return res

def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)

def sumOfNodesVal(root):
    if root is None:
        return 0
    leftSum = sumOfNodesVal(root.left)
    rightSum = sumOfNodesVal(root.right)
    return leftSum + rightSum + root.val

def countLeaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return countLeaves(root.left) + countLeaves(root.right)

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

def levelOrderTraversal(root):
    if root is None:
        return
    queue = deque([root])

    while queue:
        temp = queue.popleft()

        print(temp.val,end=" ")

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    def height_and_diameter(node):
        if not node:
            return 0, 0
        lh, ld = height_and_diameter(node.left)
        rh, rd = height_and_diameter(node.right)
        return 1 + max(lh, rh), max(ld, rd, lh + rh + 1)
    
    return height_and_diameter(root)[1] - 1

def isBalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False

def mirror(root):
    if root:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)

def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    return isMirror(root, root)

def lca(root, n1, n2):
    if not root:
        return None
    if root.val == n1 or root.val == n2:
        return root
    left_lca = lca(root.left, n1, n2)
    right_lca = lca(root.right, n1, n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca


def serialize(root):
    vals = []
    def encode(node):
        if node:
            vals.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            vals.append('#')
    encode(root)
    return ' '.join(vals)

def deserialize(data):
    vals = iter(data.split())
    def decode():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = decode()
        node.right = decode()
        return node
    return decode()

def printKthLevel(root, k):
    if not root:
        return
    if k == 0:
        print(root.val, end=" ")
        return
    printKthLevel(root.left, k-1)
    printKthLevel(root.right, k-1)


def deleteDeepest(root, d_node):
    q = [root]
    while q:
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def delete(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.val == key:
            return None
        else:
            return root
    key_node = None
    q = [root]
    temp = None
    while q:
        temp = q.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.val
        deleteDeepest(root, temp)
        key_node.val = x
    return root

root = None
root = insert(root, 1)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, -10)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, -2)

sumofNodes = sumOfNodesVal(root)
print(f"The sum of Nodes value is: {sumofNodes}")

print(f"The root value is: {root.val}")

print("Inorder traversal:")
inorderTraversal(root)
print("\nPreorder traversal:")
preorderTraversal(root)
print("\nPostorder traversal:")
postorderTraversal(root)
print("\nLevel Order Traversal:")
levelOrderTraversal(root)
print()

key = 6
print(f"\n\nSearch for {key}: {'Found' if search(root, key) else 'Not found'}")

print("\n\nHeight of tree:", height(root))

print("Diameter of the tree:", diameter(root))

print("Number of nodes in tree:", countNodes(root))

maximum = findMax(root)
print(f"The maximum value node is: {maximum}")

minimum = findMin(root)
print(f"The Minimum value node is: {minimum}")

print("Number of leaf nodes:", countLeaves(root))


print("Is tree balanced?", "Yes" if isBalanced(root) else "No")

key = 3
root = delete(root, key)
print(f"\nAfter deleting {key}:")
inorderTraversal(root)

key = -10
root = delete(root, key)
print(f"\nAfter deleting {key}:")
inorderTraversal(root)


print("\nOriginal tree Inorder Traversal:")
inorderTraversal(root)
print()

mirror(root)

print("Mirror tree Inorder Traversal:")
inorderTraversal(root)
print()

print("Is tree symmetric?", "Yes" if isSymmetric(root) else "No")

n1 = 4
n2 = 5
ancestor = lca(root, n1, n2)
print(f"Lowest Common Ancestor of {n1} and {n2}:", ancestor.val if ancestor else "None")


serialized_tree = serialize(root)
print("Serialized tree:", serialized_tree)

deserialized_tree = deserialize(serialized_tree)
print("Deserialized tree Inorder Traversal:")
inorderTraversal(deserialized_tree)
print()

k = 2
print(f"Nodes at level {k}:")
printKthLevel(root, k)
print()
