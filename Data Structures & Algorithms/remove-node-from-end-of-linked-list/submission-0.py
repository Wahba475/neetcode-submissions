class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0
        curr = head
        curr2 = head
        prev = None

        while curr:
            size += 1
            curr = curr.next

        size = size - n

        if size == 0:
            return head.next

        for i in range(size):
            prev = curr2
            curr2 = curr2.next

        prev.next = curr2.next

        return head