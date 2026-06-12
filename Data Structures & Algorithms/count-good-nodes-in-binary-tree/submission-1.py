# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque()
        q.append((root, -float('inf')))

        while q:
            node, val = q.popleft()

            if node.val >= val:
                res += 1
            
            if node.left:
                q.append((node.left, max(val, node.val)))
            if node.right:
                q.append((node.right, max(val, node.val)))
            
        return res