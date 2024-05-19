class StackUsingQueues:

    def __init__(self) :

        self.queue1 = []
        self.queue2 = []

    def push(self, item) :

        self.queue1.append(item)

    def pop(self) :

        if not self.queue2 :
            self._transfer()
        return self.queue2.pop()

    def _transfer(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1

    def isEmpty(self):
        return self.queue1 and self.queue2
    
    def display(self) :

        print(self.queue1)

stack = StackUsingQueues()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

stack.display()
stack.pop()
stack.display()

