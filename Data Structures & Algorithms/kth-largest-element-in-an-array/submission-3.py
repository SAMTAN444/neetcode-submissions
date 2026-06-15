class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-n for n in nums]

        heapq.heapify(num)

        while k > 1:
            heapq.heappop(num)
            k -= 1
        
        return -num[0]