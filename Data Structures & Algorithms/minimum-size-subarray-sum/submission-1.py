class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # GOAL: to return the length of the smallest subarray that has the elements
        # summing up to be equal to or greater than the target
        # stop and update min_sub when sum of array >= target
        # move r (inc sum)= when subarray sum is less than 10
        # move l (dec sum)= when sub sum is greater than 10 -> we want a smaller subarray
        #  target = 10, nums = [1,1,2,3,5,5] 
        #                               l
        #                                 r
        # curr_sum = 1
        # ms = 1
        l = 0
        r = 0
        curr_sum = 0
        min_sub = float('inf')
        while r < len(nums):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_sub = min(min_sub, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            r += 1
        return min_sub if min_sub != float('inf') else 0


            


