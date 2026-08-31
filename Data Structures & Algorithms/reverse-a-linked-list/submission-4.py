# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        # 10 20 30 
        while cur != None:
            tmp = cur.next #20 30
            cur.next = prev 
            prev = cur #10 
            cur = tmp #20
        
        return prev 
