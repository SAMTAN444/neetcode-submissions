class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = []
        if zero_cnt == 1:
            for num in nums:
                if not num:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(prod // num)
        return res