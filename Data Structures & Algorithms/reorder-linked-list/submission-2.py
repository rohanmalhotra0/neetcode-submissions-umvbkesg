class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        currHead = head

        while currHead and currHead.next and currHead.next.next:
            # Find node right before the last node
            curr = currHead

            while curr.next.next:
                curr = curr.next

            # Remove last node
            put = curr.next
            curr.next = None

            # Put last node after currHead
            put.next = currHead.next
            currHead.next = put

            # Move inward
            currHead = put.next