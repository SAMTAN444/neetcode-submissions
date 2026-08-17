class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod = 0, 1

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num
        
        if zero_cnt > 1:
            return len(nums) * [0]
        
        res = []

        if zero_cnt == 1:
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(prod // num)
        return res