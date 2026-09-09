# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        curr = head
        while curr.val != n and curr.next:
            prev = curr
            curr = curr.next
        if curr.val == n:
            prev.next = prev.next.next
            curr.next = None
            return head
        else:
            return None
        