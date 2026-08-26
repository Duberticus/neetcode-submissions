# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#linkedList = [10,20,30]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #curr = head

        prev, curr = None, head
        # prev is now null and the current node is 10, it is also the head
        while curr != None:
            nxt = curr.next
            #save 20 as a temp variable// next iteration we save 30 as the tmp
            curr.next = prev
            #the next node is now null //next is now 10
            prev = curr
            #the previous node now 10 //previous is now 20
            curr = nxt
            #current is [20] //next is set to 30

        return prev