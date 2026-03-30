class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = 0
        for i in range(len(nums)):
            if nums[i] < nums[small]:
                small = i
        return nums[small]