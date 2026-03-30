class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num1 + num2 = target
        # num1 = target - num2 
        num_indices = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_indices:
                return [num_indices[diff], i]
            num_indices[n] = i
            

