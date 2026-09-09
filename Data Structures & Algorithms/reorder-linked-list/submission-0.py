# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        curr = dummy
        while curr.next.next:
            curr = curr.next 
        #5
        put = curr.next #6
        curr.next = None # 5 -> None: End the list


        # 0=Head  1 2
        put.next = head.next # 6 -> 1
        head.next = put
        return head

