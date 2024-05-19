class QueueUsingStack:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    def enqueue(self,data) :

        self.stack1.append(data)

    def dequeue(self) :

        if not self.stack1 and not self.stack2 :

            return f"The Queue is empty"
        
        if not self.stack2 :

            while self.stack1 :
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Queue is empty")  # Added this check
        
        return self.stack2.pop()
    
    def display(self):
        # Display elements in stack2 (in correct order)
        print("Queue:", end=" ")
        for elem in self.stack2:
            print(elem, end=" ")

        # Display elements in stack1 (in reverse order)
        for elem in reversed(self.stack1):
            print(elem, end=" ")
        print()


q = QueueUsingStack()

for i in range(6):

    q.enqueue(i)

q.display()
print(q.dequeue())  # Output: 3
print(q.dequeue())  # Output: 3

q.display()


