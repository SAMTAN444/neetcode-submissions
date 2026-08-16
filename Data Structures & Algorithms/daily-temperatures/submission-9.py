class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                cn, ci = stack.pop()
                res[ci] = i - ci
            
            stack.append([num, i])
        return res