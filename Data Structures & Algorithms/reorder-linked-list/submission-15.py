# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head

        node = []
        while curr:
            node.append(curr)
            curr = curr.next
        
        length = len(node)

        l, r = 0, length - 1

        while l < r:
            node[l].next = node[r]
            l += 1
            if l > r:
                break
            node[r].next = node[l]
            r -= 1
        node[l].next = None
    