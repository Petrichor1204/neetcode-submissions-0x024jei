class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums) 

        res = [0] * len(nums)
        for c, n in enumerate(nums):
            if zero_cnt: res[c] = 0 if n else prod
            else: res[c] = prod // n
        return res
            
