# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head):
        current = head.next

        newList = []
        sumOfNodes = 0
        while current:

            if current.val != 0:
                sumOfNodes += current.val
            else:
                newList.append(sumOfNodes)
                sumOfNodes = 0
            current = current.next
        def array_to_linklist(listx):
            dummy_head = ListNode(0)
            current = dummy_head
            for value in listx:
                current.next = ListNode(value)
                current = current.next
            return dummy_head.next
        return array_to_linklist(newList)
        

        
             
