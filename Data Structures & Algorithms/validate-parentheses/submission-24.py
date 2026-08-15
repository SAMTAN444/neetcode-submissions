class Solution:
    def isValid(self, s: str) -> bool:
        closedInOpen = {"}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c in closedInOpen:
                if stack and stack[-1] == closedInOpen[c]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0