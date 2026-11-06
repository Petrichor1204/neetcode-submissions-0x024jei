class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob the first but not last house
        # rob the last but not first house
        # nums = [9,8,3,6] [2,9,8,3] a = 12   b = 15  t = 12
        #               i
        if len(nums) <= 2:
            return max(nums)

        def max_robbed(nums):
            a, b = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                temp = b 
                b, a = max(temp, a + nums[i]), temp

            return b

        return max(max_robbed(nums[1:]), max_robbed(nums[:-1]))