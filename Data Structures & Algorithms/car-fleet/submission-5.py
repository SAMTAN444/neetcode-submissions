class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            time = (target-p) / s
            if len(stack) >= 1 and time <= stack[-1]:
                val = max(stack.pop(), time)
                stack.append(val)
            else:
                stack.append(time)
        return len(stack)
