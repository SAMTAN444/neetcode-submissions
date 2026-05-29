class Solution:
    def isValid(self, s: str) -> bool:
        ss = []
        closedInOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closedInOpen:
                if ss and closedInOpen[c] == ss.pop():
                    continue
                else:
                    return False
            else:
                ss.append(c)
        return True if not ss else False