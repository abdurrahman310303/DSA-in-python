class MinHeap :

    def __init__(self) :

        self.heap = []
    

    def parent (self, index):
        return (index - 1) // 2

    def leftChild(self,index):

        return 2* index +1
    
    def rightChild(self,index):

        return 2 * index +2
    
    def insert(self,data):

        self.heap.append(data)

        self.heapifyUp(len(self.heap) - 1)
    
    def heapifyUp(self,index):

        parent_index = self.parent(index)

        if index > 0 and self.heap[parent_index] > self.heap[index]:

            self.heap[parent_index],self.heap[index] = self.heap[index],self.heap[parent_index]

            self.heapifyUp(parent_index)
    
    def heapifyDown(self,index):

        smallest = index

        left = self.leftChild(index)
        right = self.rightChild(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:

            smallest = right
        
        if smallest != index:

            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            self.heapifyDown(smallest)
        
    def getMin(self) :

        if self.heap is None:

            return
        else:
            return self.heap[0]
    
    def getSize(self) :

        return len(self.heap)



minheap = MinHeap()

minheap.insert(1)
minheap.insert(2)
minheap.insert(3)
minheap.insert(4)
minheap.insert(5)

print("The size of heap is " + str(minheap.getSize()))
print("The Min of heap is "+ str(minheap.getMin()))

        














# class MinHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, i):
#         return (i - 1) // 2

#     def left_child(self, i):
#         return 2 * i + 1

#     def right_child(self, i):
#         return 2 * i + 2

#     def insert(self, key):
#         self.heap.append(key)
#         self._heapify_up(len(self.heap) - 1)

#     def extract_min(self):
#         if len(self.heap) == 0:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
    
#         root = self.heap[0]
#         self.heap[0] = self.heap.pop()
#         self._heapify_down(0)
        
#         return root

#     def _heapify_up(self, index):
#         parent_index = self.parent(index)
#         if index > 0 and self.heap[index] < self.heap[parent_index]:
#             self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
#             self._heapify_up(parent_index)

#     def _heapify_down(self, index):
#         smallest = index
#         left = self.left_child(index)
#         right = self.right_child(index)
        
#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != index:
#             self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
#             self._heapify_down(smallest)

#     def get_min(self):
#         if len(self.heap) == 0:
#             return None
#         return self.heap[0]

#     def size(self):
#         return len(self.heap)

# # Example usage
# min_heap = MinHeap()
# min_heap.insert(3)
# min_heap.insert(1)
# min_heap.insert(6)
# min_heap.insert(5)
# min_heap.insert(2)
# min_heap.insert(4)

# print("Min element:", min_heap.get_min())  # Output: Min element: 1
# print("Extract min:", min_heap.extract_min())  # Output: Extract min: 1
# print("Min element:", min_heap.get_min())  # Output: Min element: 2
