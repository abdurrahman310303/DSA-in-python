# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse (head):

    current = head
    prev = None

    while current:

        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev
class Solution:
    def addTwoNumbers(self, l1, l2):

        firstnum = secondnum = ""

        l1 = reverse(l1)
        l2 = reverse(l2)

        

        while l1 or l2:
            if l1:
                firstnum += str(l1.val)
                l1 = l1.next
            if l2:
                secondnum += str(l2.val)
                l2 = l2.next


        result = int(firstnum) + int(secondnum)
        print("the resutl str is "+str(result))
        result_str = str(result)

        

        result_list = ListNode()

        current = result_list

        for char in result_str:
            current.next = ListNode(str(char))
            current = current.next

        reverseResult = reverse(result_list.next)
        return reverseResult
