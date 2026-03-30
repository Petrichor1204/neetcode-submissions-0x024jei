class Solution:
    
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                # Minimum must be to the right
                l = m + 1
            else:
                # Minimum is at mid or to the left
                r = m
        return nums[l]
