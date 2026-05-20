class Solution:
    def isValid(self, h: str) -> bool:
        s = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in h:
            if c in closeToOpen:
                if s and s[-1] == closeToOpen[c]:
                    s.pop()
                else:
                    return False
            else:
                s.append(c)
        return True if not s else False