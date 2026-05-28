class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l, r = 0, len(heights) - 1

        while l < r:
                h = min(heights[l], heights[r])
                area = h * (r-l)
                m = max(area, m)
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        return m