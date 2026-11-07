class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return the kth largest element
        # [1,2,3,4,5]
        nums.sort()
        return nums[len(nums) - k]
    

    