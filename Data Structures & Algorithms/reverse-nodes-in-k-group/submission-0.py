class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 1. Find the kth node in this group
            kth = self.getKth(groupPrev, k)

            # Not enough nodes left
            if not kth:
                break

            # 2. Save where the next group starts
            groupNext = kth.next

            # 3. Reverse the current group
            groupStart = groupPrev.next

            newHead, newTail = self.reverseGroup(
                groupStart,
                groupNext
            )

            # 4. Connect previous group to reversed group
            groupPrev.next = newHead

            # 5. Move groupPrev forward
            groupPrev = newTail

        return dummy.next


    def getKth(self, curr, k):
        """Return the kth node after curr."""
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr


    def reverseGroup(self, start, stop):
        """
        Reverse nodes starting at 'start'
        until reaching 'stop'.

        stop itself is NOT reversed.

        Returns:
            newHead
            newTail
        """

        prev = stop
        curr = start

        while curr != stop:
            nextNode = curr.next

            curr.next = prev

            prev = curr
            curr = nextNode

        # prev = new head
        # start = new tail
        return prev, start