# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None:
            return

        curr = head
        slow = head
        fast = head.next

        # Find the end of the first half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev = None

        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # Merge the two halves
        while prev:
            Nextcurr = curr.next
            Nextprev = prev.next

            curr.next = prev
            prev.next = Nextcurr

            curr = Nextcurr
            prev = Nextprev

        return