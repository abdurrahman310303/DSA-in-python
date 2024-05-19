class Node :

    def __init__(self,data) :

        self.value = data
        self.next = None

class Queue :

    def __init__(self) :

        self.front = None
        self.rear = None
    

    def enqueue (self,newData) :

        newNode = Node(newData)

        if self.front is None:

            self.front = self.rear = newNode
        
        else:

            self.rear.next = newNode
            self.rear = newNode
    
    def dequeue (self) :

        if self.front is None :
            return f"the Queue is empty "
        
        self.front = self.front.next

        if self.front is None:

            self.rear = None

    def display(self) :

        current = self.front

        while current :

            print(current.value,end=" ")
            current = current.next


if __name__ == "__main__" :

    queue = Queue()


    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)

    queue.dequeue()

    queue.display()
        

            