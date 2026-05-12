class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod = 0, 1
        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        r = []
        if zero_cnt == 1:
            for num in nums:
                if num == 0:
                    r.append(prod)
                else:
                    r.append(0)
        else:
            for num in nums:
                r.append(prod // num)
        return r