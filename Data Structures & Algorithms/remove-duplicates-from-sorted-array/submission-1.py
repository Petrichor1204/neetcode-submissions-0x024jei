class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # understand: given an arr of duplicates, maintain order of arr but remove duplicates and return num of unique elements as k
        # nums = [1,2,3,3,4]
        #             l 
        #               r
        # 
        l, r = 0, 0
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            l += 1
        return l 

       

         