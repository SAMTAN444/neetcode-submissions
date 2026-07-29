class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-num for num in nums]

        heapq.heapify(num)
    
        while k > 1:
            heapq.heappop(num)
            k -= 1
        
        res = heapq.heappop(num)
        return -res