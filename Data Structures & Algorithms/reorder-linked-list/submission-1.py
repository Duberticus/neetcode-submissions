# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        newList = []

        while arr:
            newList.append(arr.pop(0))

            if arr:
                newList.append(arr.pop())

            curr = head

            for value in newList:
                curr.val = value
                curr = curr.next

        return curr






                