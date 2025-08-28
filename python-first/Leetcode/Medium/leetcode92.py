# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        if left >= right or head is None:
            return head
        
        current = head 
        prev = None
        i = 1
        
        while i<left:

            prev = current
            current = current.next
            i +=1
        
        rtail = current
        rhead = None

        while i<=right:

            temp = current.next
            current.next = rhead 
            rhead = current
            current = temp 
            i +=1
        
        rtail.next = current

        if prev:
            
            prev.next = rhead
        else:
            head = rhead
        

        return head
        
        
        