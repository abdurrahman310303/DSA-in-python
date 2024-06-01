# • Insert a node into the BST.
# • Search for a specific value in the BST. 
# • Delete a node from the BST. 
# • Print the elements of the BST in pre-order traversal.

class Node:

    def __init__(self,value):

        self.left = None
        self.right = None
        self.val = value

class Lab8_BST :

    def __init__(self):

        self.root = None
    
    def insert(self,value):

        self.root = self._insert(self.root,value)
    
    def _insert(self,node,value):

        if not node:
             node = Node(value)
        
        if value < node.val:
            node.left = self._insert(node.left,value)
        elif(value > node.val):
            node.right = self._insert(node.right,value)
        return node
    
    def search(self,value):

        return self._search(self.root,value)
    
    def _search(self,node,value):

        if not node:
            return False
        
        if value < node.val:

            return self._search(node.left,value)
        elif value > node.val:
            return self._search(node.right,value)
        
        return True
    
    def delete(self,value):

        self.root = self._delete(self.root, value)
    
    def _delete(self,node,val):

        if not node:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._find_min(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    
    def _find_min(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current


        
    
    def preOrderTraversal (self):

        self._preOrderTraversal(self.root)

    def _preOrderTraversal (self,node):

        if node:

            print(str(node.val),end=" ")
            self._preOrderTraversal(node.left)
            self._preOrderTraversal(node.right)


bst = Lab8_BST()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(18)
bst.insert(6)

bst.preOrderTraversal()

print()
print(bst.search(2))

bst.delete(12)
print()
bst.preOrderTraversal()



