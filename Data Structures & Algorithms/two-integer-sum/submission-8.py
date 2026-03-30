class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num1 + num2 = target
        # num2 = target - num1
        num_dict = {} #num: index

        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in num_dict:
                return [num_dict[num2], i]
            num_dict[nums[i]] = i
        return []