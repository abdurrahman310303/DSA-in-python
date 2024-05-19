class Stack :

    def __init__(self) :

        self.values = []

    def push (self, item) :

        self.values.append(item)
    
    def pop(self) :

        if not self.values :
            return "the stack is empty"
        
        else :
            return self.values.pop()
    
    def getTop(self) :

        if not self.values :
            return "the stack is empty"
        else:
            return self.values[-1]

if __name__ == "__main__" :

    stack = Stack()

    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.push('d')

    print("the top of the stack is  " + stack.getTop())
    print("Popped  " + stack.pop())
    print("the top of the stack is  " + stack.getTop())
    while stack.values :

        print(stack.pop())
