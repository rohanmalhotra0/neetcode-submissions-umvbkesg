# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0 
        if not head:
            return None
        newHead = head    
        curr = head.next 
        while curr != None:
            temp = curr.next
            curr.next = newHead
            curr = temp 
            newHead = newHead.next

