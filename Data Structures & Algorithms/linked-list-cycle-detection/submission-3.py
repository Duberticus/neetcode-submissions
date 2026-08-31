# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head2 = head
        head = head

        while head2 is not None and head2.next is not None:
            head = head.next
            head2 = head2.next.next

            if head == head2:
                return True

        return False
        
