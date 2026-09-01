# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ansList = ListNode()
        tmp = ansList

        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                #add list 1 val to ansList
                ansList.next = list1
                list1 = list1.next
            else:
                #add list 2 val to ansList
                ansList.next = list2
                list2 = list2.next

            ansList = ansList.next

        if list1 == None :
            #add list 2 val to ansList
            ansList.next = list2
        else:
            #add list 1 to ansList
            ansList.next = list1

        return tmp.next
