# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        currHead = head

        while currHead and currHead.next and currHead.next.next:

            curr = currHead

            # Find second-to-last node
            while curr and curr.next and curr.next.next:
                curr = curr.next

            # Take last node
            put = curr.next

            # Cut it off 
            curr.next = None

            # Insert it after currHead
            put.next = currHead.next
            currHead.next = put

            # Move inward
            currHead = put.next