class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(nums) != len(numset):
            return True
        return False