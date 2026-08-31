# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        init = ListNode()
        toStore = init

        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                toStore.next = head1
                head1 = head1.next
        # return toRet


            elif head1.val > head2.val:
                toStore.next = head2
                head2 = head2.next 
        #  return toRet

            toStore = toStore.next
        #for leftovers
        if head1 != None:
            toStore.next = head1
        else:
            toStore.next = head2

        return init.next