class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            top = min(heights[l], heights[r])
            area = (r-l) * top
            res = max(area, res)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
