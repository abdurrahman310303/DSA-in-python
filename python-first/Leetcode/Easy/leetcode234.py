# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse (head) :

    current = head
    prev = None

    while current:

        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

class Solution:
    def isPalindrome(self, head):

        if head is None and head.next is None:
            return True
        
        slow = fast = head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next
        
        second_half = reverse(slow.next)

        p1,p2 = head,second_half

        while p2:

            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
        