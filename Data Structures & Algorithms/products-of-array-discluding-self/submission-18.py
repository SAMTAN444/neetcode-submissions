class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        for num in nums:
            if not num:
                zero_cnt += 1
            else:
                prod *= num
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = []
        if zero_cnt == 1:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(prod)
        else:
            for num in nums:
                res.append(prod // num)

        return res