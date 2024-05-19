class Queue :

    def __init__(self) :

        self.queue = []

    def enqueue (self,value) :

        self.queue.append(value)
    
    def dequeue(self) :

        if len(self.queue) < 1:
            return f"The queue is empty " 
        else:
            front = self.queue[0]

            self.queue = self.queue[1:]
            return front
    def display(self) :
        print(self.queue)


if __name__ == "__main__" :

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print("Dequeued : " + str(queue.dequeue()))
    print("Dequeued : " + str(queue.dequeue()))


    queue.display()
    