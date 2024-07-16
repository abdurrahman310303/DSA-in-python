class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                duplicate_value = current.data
                while current and current.data == duplicate_value:
                    current = current.next
                self.head = current
            else:
                break
        if not current:
            return
        prev, current = current, current.next
        while current and current.next:
            if current.data == current.next.data:
                duplicate_value = current.data
                while current and current.data == duplicate_value:
                    current = current.next
                prev.next = current
            else:
                prev, current = current, current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(5)
ll.append(6)

print("Original Linked List:")
ll.print_list()

ll.delete_duplicates()

print("Linked List after deleting duplicates:")
ll.print_list()
