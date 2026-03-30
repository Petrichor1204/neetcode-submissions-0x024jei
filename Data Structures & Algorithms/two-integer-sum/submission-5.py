class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num1 + num2 = target
        # num1 = target - num2 
        num_indices = {}
        for i, n in enumerate(nums):
            num_indices[n] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_indices and num_indices[diff] != i:
                return [i, num_indices[diff]] 
            

