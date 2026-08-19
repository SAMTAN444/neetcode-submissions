# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        a = []

        while curr:
            a.append(curr)
            curr = curr.next
        
        length = len(a)

        i, j = 0, length - 1

        while i < j:
            a[i].next = a[j]
            i += 1
            if i < j:
                a[j].next = a[i]
                j -= 1
        a[i].next = None
