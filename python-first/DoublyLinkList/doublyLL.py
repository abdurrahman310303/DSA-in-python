class Node :

    def __init__(self,data) :

        self.data = data
        self.next = None
        self.prev = None

class DoublyLinklist :

    def __init__(self) :

        self.head = None
    

    def insertAtStart (self,new_data) :

        new_node = Node(new_data)

        if self.head is None :

            self.head = new_node
            return
        
        new_node.next = self.head

        self.head.prev = new_node

        self.head = new_node
    
    def insertAtEnd (self,new_data) :

        new_node = Node(new_data)

        if self.head is None :
            self.head = new_node
            return
        
        temp = self.head 

        while temp.next :
            temp = temp.next
        
        temp.next = new_node

        new_node.prev = temp

    def delete(self, key) :

        current = self.head

        if current.data == key and current.next is None :

            self.head = None
            return
        
        if current.data == key :

            self.head = current.next

            self.head.prev = None
            return
        
        while current :

            if current.data == key :
                break
            current = current.next
        
        if current.next :

            current.prev.next = current.next
            current.next.prev = current.prev
            return
        
        if current.data == key :
            current.prev.next = None

    def printList(self) :

        temp = self.head 

        while temp :

            print(temp.data)

            temp = temp.next 


if __name__ == "__main__" :

    dl = DoublyLinklist()

    dl.insertAtStart(1)
    dl.insertAtStart(2)
    dl.insertAtStart(3)
    dl.insertAtEnd(0)
    dl.insertAtStart(4)


    dl.delete(0)

    dl.printList()