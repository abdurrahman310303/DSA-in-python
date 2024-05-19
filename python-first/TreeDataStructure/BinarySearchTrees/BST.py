# class TreeNode:

#     def __init__(self,val=0,left=None,right=None):

#         self.left = left
#         self.right = right
#         self.val = val

# class BST:

#     def __init__(self):
#         self.root = None
    

#     def insert(self,val):

#         self.root = self._insert(self.root,val)
    
#     def _insert(self, node, val):
#         if not node:
#             return TreeNode(val)
        
#         if val < node.val:
#             node.left = self._insert(node.left, val)
#         elif val > node.val:
#             node.right = self._insert(node.right, val)

#         return node
    
#     def search (self,val) :

#         return self._search(self.root,val)
    
#     def _search (self,node,val):

#         if not node:

#             return False
        
#         if val < node.val:

#             return self._search(node.left,val)
        
#         elif val > node.val :

#             return self._search(node.right,val)
        
#         return True

#     def isBalanced(self):

#         return self._isBalanced(self.root)
    
#     def _isBalanced(self,node):

#         if not node :
            
#             return True
#         lh = self._isBalanced(node.left)
#         rh = self._isBalanced(node.right)

#         if lh is False or rh is False or abs(lh - rh) > 1:

#             return False
        
#         return 1+max(lh,rh)
        

#     def inorder(self):

#         self._inorder(self.root)
    
#     def _inorder(self,node):

#         if node:

#             self._inorder(node.left)
#             print(str(node.val),end=" ")
#             self._inorder(node.right)
    
#     def preorder(self):

#         self._preorder(self.root)
    
#     def _preorder(self,node):

#         if node:
#             print(str(node.val),end=" ")
#             self._preorder(node.left)
#             self._preorder(node.right)

#     def postorder(self):

#         self._postorder(self.root)
    
#     def _postorder(self,node):
        
#         if node:
#             self._postorder(node.left)
#             self._postorder(node.right)
#             print(str(node.val),end=" ")

        


# if __name__ == "__main__":

#     bst = BST()

#     bst.insert(3)
#     bst.insert(1)
#     bst.insert(2)
#     bst.insert(4)
#     bst.insert(5)




#     print("In Order Traversal : " ,end=" ")
#     bst.inorder()


#     print("\n")
#     print("Pre Order Traversal : " ,end=" ")

#     bst.preorder()

#     print("\n")
#     print("Post Order Traversal : " ,end=" ")

#     bst.postorder()

#     print("\n")
#     print("Found : " + str(bst.search(9)))

#     print("\n")
#     print("IsBalanced : " + str(bst.isBalanced()))

class TreeNode :

    def __init__(self,val,left = None,right = None):

        self.val = val
        self.left = left
        self.right = right

class BST :

    def __init__(self):
        self.root = None
    
    def insert(self,val):

        self.root = self._insert(self.root,val)
    
    def _insert(self, node, val) :

        if not node:

            return TreeNode(val)
        
        if val < node.val:

            node.left = self._insert(node.left,val)
        
        elif val > node.val:

            node.right = self._insert(node.right,val)
        return node
    
    def search(self,val):

        return self._search(self.root,val)
    
    def _search(self,node,val):

        if not node:

            return False
        
        if node.val < val:

            return self._search(node.left,val)
        
        elif node.val > val:

            return self._search(node.right,val)
        
        return True
    
    def delete(self, val):

        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
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
    
    def find_min(self):
        node = self._find_min(self.root)
        return node.val if node else None
    
    def _find_min(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current
    
    def find_max(self):
        node = self._find_max(self.root)
        return node.val if node else None
    
    def _find_max(self, node):
        current = node
        while current and current.right:
            current = current.right
        return current
    
    def inorder(self):

        self._inorder(self.root)
    
    def _inorder(self,node):

        if node:

            self._inorder(node.left)
            print(node.val,end=" ")
            self._inorder(node.right)


if __name__ == "__main__" :

    bst = BST()

    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)


    bst.inorder()
    

    print("\nFound : "+str(bst.search(1)))


    bst.delete(3)
    print("After Deletion : ",end=" ")

    bst.inorder()
    print("\n")
    print("Minimum : " + str(bst.find_min()))
    print("maximum : " + str(bst.find_max())) 
    


