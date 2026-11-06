class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob the first but not last house
        # rob the last but not first house
        # nums = [9,8,3,6] [2,9,8,3] [9,9,12,15] [2,9,10,12] 
        #                         i
        if len(nums) <= 2:
            return max(nums)

        def max_robbed(nums):

            memo = [0] * len(nums)

            for i in range(len(nums)):
                memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])

            return memo[-1]

        return max(max_robbed(nums[1:]), max_robbed(nums[:-1]))