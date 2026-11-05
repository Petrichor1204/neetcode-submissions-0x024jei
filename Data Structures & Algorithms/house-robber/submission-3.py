class Solution:
    def rob(self, nums: List[int]) -> int:
        # [2,9,8,3,6]
        #  i 
        # option 1 = 16
        # option 2 = 12
        # at every stop - take current in addition to prev without adj or take prev with adj without current
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)
            
        memo = [0] * len(nums) #[0,0,0]

        for i in range(len(nums)):
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])

        return memo[-1]

            
