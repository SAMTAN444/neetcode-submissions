# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        
        curr = head
        removeIndex = l - n

        if removeIndex == 0:
            return head.next
        
        for i in range(l-1):
            if (i+1) == removeIndex:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head