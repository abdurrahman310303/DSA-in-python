class MinStack :

    def __init__(self) :

        self.stack = []
        self.minStack = []

    def push (self, value) :

        self.stack.append(value)

        if not self.minStack or value <= self.minStack[-1] :
            self.minStack.append(value)

    def pop(self) :
        
        if self.stack.pop() == self.minStack[-1] :
            self.minStack.pop()
    def getMin(self) :

        return self.minStack[-1]
    
    
if __name__ == "__main__" :

    stack = MinStack()

    stack.push(1)
    stack.push(2)

    print("The minimum is : "+str(stack.getMin()))
    while stack.stack :
        print(str(stack.stack.pop()))