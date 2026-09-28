# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        curr = head
        curr2 = head
        while curr and n != k:
            prev = curr
            curr = curr.next
            n += 1
        
        prev.next = None #3
        curr.next = curr2 #6 --> 1
        
        return curr