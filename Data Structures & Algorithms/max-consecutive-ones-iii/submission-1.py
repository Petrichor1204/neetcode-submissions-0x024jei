class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0
        l = 0
        turned = 0

        if not nums:
            return 0

        for r in range(len(nums)):
            if nums[r] == 0:
                turned += 1

            while turned > k:
                if nums[l] == 0:
                    turned -= 1
                l += 1
                

            if (r - l + 1) > maxLen:
                maxLen = (r - l + 1)

        return maxLen