# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr=head
        curr2=head
        count=0

        while curr:
            curr=curr.next
            count+=1


        count = count // 2

        while count:
            curr2 = curr2.next
            count -= 1

        return curr2
