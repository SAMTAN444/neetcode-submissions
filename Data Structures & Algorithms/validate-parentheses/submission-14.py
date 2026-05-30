class Solution:
    def isValid(self, s: str) -> bool:
        closedInOpen = {"]": "[", "}": "{", ")": "("}
        stack = []
        for c in s:
            if c in closedInOpen:
                if stack and stack.pop() == closedInOpen[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False