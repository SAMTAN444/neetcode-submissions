# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []

        curr = head
        while curr:
            temp.append(curr)
            curr = curr.next
        
        i, j = 0, len(temp) - 1
        while i < j:
            temp[i].next = temp[j]
            i = i + 1
            temp[j].next = temp[i]
            j -= 1
        temp[i].next = None
        