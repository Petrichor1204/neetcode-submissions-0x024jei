class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            l, r = i + 1, len(nums) - 1
            # while loop for l and r => l < r
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    curr_list = [nums[i], nums[l], nums[r]]
                    final_list.append(curr_list)
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return final_list


