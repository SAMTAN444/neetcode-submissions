class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedInOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closedInOpen:
                if stack and closedInOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False