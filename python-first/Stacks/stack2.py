class Node :

    def __init__(self,value) :

        self.value = value
        self.next = None
    
class Stack :

    def __init__(self) :

        self.top = None
    
    def push(self, item) :

        newNode = Node(item)

        newNode.next = self.top
        self.top = newNode
    
    def pop(self) :
        
        poped = self.top
        if self.top is None:
            return "the stack is empty"
        
        else:

            self.top = self.top.next
            return poped.value
        
    def getTop(self) :

        if self.top is None:
            return "the stack is empty"
        return self.top.value
    


if __name__ == "__main__" :

    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Popped Data " + str(stack.pop()))

    while stack.top :
        print(stack.pop())
# class Node :

#     def __init__(self,value) :

#         self.data = value
#         self.next = None

# class Stack :

#     def __init__(self) :
#         self.top = None
    
#     def push (self,val) :

#         newNode = Node(val)

#         newNode.next = self.top

#         self.top = newNode
    
#     def pop (self) :    
#         poped = self.top
#         if self.top is None :

#             return f'Stact is Empty'
        
#         else :

#             self.top = self.top.next
#             return poped.data
    
#     def topStack(self) :

#         if self.top is None :
#             return f"the stack is empty"
#         else:
#             return self.top.data

# if __name__ == "__main__" :

#     sobj = Stack()

#     sobj.push('1')
#     sobj.push('2')
#     sobj.push('3')

#     print("Popped : " + sobj.pop() )
#     print("Popped : " + sobj.pop() )
#     print("Popped : " + sobj.pop() )
#     print("Popped : " + sobj.pop() )
#     print("Top : " + sobj.topStack() )
#     while sobj.top :
#         print(sobj.pop())