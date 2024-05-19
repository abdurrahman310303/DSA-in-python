class TreeNode:

    def __init__(self,val=0,left=None,right=None):

        self.left = left
        self.right = right
        self.val = val

class BST:

    def __init__(self):
        self.root = None
    

    def insert(self,val):

        self.root = self._insert(self.root,val)
    
    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)

        return node
    
    def search (self,val) :

        return self._search(self.root,val)
    
    def _search (self,node,val):

        if not node:

            return False
        
        if val < node.val:

            return self._search(node.left,val)
        
        elif val > node.val :

            return self._search(node.right,val)
        
        return True

    def isBalanced(self):

        return self._isBalanced(self.root)
    
    def _isBalanced(self,node):

        if not node :
            
            return True
        lh = self._isBalanced(node.left)
        rh = self._isBalanced(node.right)

        if lh is False or rh is False or abs(lh - rh) > 1:

            return False
        
        return 1+max(lh,rh)
        

    def inorder(self):

        self._inorder(self.root)
    
    def _inorder(self,node):

        if node:

            self._inorder(node.left)
            print(str(node.val),end=" ")
            self._inorder(node.right)
    
    def preorder(self):

        self._preorder(self.root)
    
    def _preorder(self,node):

        if node:
            print(str(node.val),end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):

        self._postorder(self.root)
    
    def _postorder(self,node):
        
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.val),end=" ")

        


if __name__ == "__main__":

    bst = BST()

    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)




    print("In Order Traversal : " ,end=" ")
    bst.inorder()


    print("\n")
    print("Pre Order Traversal : " ,end=" ")

    bst.preorder()

    print("\n")
    print("Post Order Traversal : " ,end=" ")

    bst.postorder()

    print("\n")
    print("Found : " + str(bst.search(9)))

    print("\n")
    print("IsBalanced : " + str(bst.isBalanced()))


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self,val) :

#         self.root = self._insert(self.root,val)
    
#     def _insert(self,node,val) :

#         if not node:
#             return TreeNode(val)
        
#         if val <= node.val:

#             node.left = self._insert(node.left,val)
#         elif val >= node.val:
#             node.right = self._insert(node.right,val)

#         return node
#     # def insert(self, val):
#     #     self.root = self._insert(self.root, val)

#     # def _insert(self, node, val):
#     #     if not node:
#     #         return TreeNode(val)
#     #     if val < node.val:
#     #         node.left = self._insert(node.left, val)
#     #     elif val > node.val:
#     #         node.right = self._insert(node.right, val)
#     #     return node

#     def delete(self, val):
#         self.root = self._delete(self.root, val)

#     def _delete(self, node, val):
#         if not node:
#             return None
#         if val < node.val:
#             node.left = self._delete(node.left, val)
#         elif val > node.val:
#             node.right = self._delete(node.right, val)
#         else:
#             if not node.left:
#                 return node.right
#             if not node.right:
#                 return node.left
#             temp = self._find_min(node.right)
#             node.val = temp.val
#             node.right = self._delete(node.right, temp.val)
#         return node

#     def _find_min(self, node):
#         while node.left:
#             node = node.left
#         return node

#     def search(self, val):
#         return self._search(self.root, val)

#     def _search(self, node, val):
#         if not node:
#             return False
#         if val < node.val:
#             return self._search(node.left, val)
#         elif val > node.val:
#             return self._search(node.right, val)
#         else:
#             return True

#     def inorder(self):
#         self._inorder(self.root)
#         print()

#     def _inorder(self, node):
#         if node:
#             self._inorder(node.left)
#             print(node.val, end=' ')
#             self._inorder(node.right)

#     def preorder(self):
#         self._preorder(self.root)
#         print()

#     def _preorder(self, node):
#         if node:
#             print(node.val, end=' ')
#             self._preorder(node.left)
#             self._preorder(node.right)

#     def postorder(self):
#         self._postorder(self.root)
#         print()

#     def _postorder(self, node):
#         if node:
#             self._postorder(node.left)
#             self._postorder(node.right)
#             print(node.val, end=' ')

# # Example usage
# bst = BST()
# bst.insert(1)


# bst.insert(2)
# bst.insert(3)
# bst.insert(4)
# # bst.insert(4)
# # bst.insert(6)
# # bst.insert(8)

# print("Inorder traversal:")
# bst.inorder()

# print("Preorder traversal:")
# bst.preorder()

# print("Postorder traversal:")
# bst.postorder()

# # print("Deleting 2:")
# # bst.delete(2)
# # bst.inorder()

