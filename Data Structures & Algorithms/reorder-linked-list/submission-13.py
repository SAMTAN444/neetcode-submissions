# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = []
        cur = head
        while cur:
            temp.append(cur)
            cur = cur.next
        
        i, j = 0, len(temp) - 1

        while i < j:
            temp[i].next = temp[j]
            i += 1
            if i >= j:
                break
            temp[j].next = temp[i]
            j -= 1
        temp[i].next = None
