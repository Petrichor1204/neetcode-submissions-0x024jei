class Solution:
    def findMin(self, nums: List[int]) -> int:
        numssort = sorted(nums)
        return numssort[0]