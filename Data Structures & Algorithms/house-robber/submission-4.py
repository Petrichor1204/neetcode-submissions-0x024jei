class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]
        #      i 
        # a = 2
        # b = 9
        # [2,9,10,12,16]
        # at every stop - take current in addition to prev without adj or take prev with adj without current
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        a, b = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            a, b = b, max(b, nums[i] + a)

        return b

            
