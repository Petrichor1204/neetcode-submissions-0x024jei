class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # goal: return an array of the triplets that sum up to 0
        # nums = [-1,0,1,2,-1,-4]
                # {-4:0, -1:1, -1:2, 0:3, 1:4, 2:5}
                #[-4,-1,-1,0,1,2]
                #  i
                #     l
                #              r
                # [[-1,-1,2], [-1,0,1]]
        # what to do when triplet has been seen before?
        result = []
        nums.sort()

        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                
                if target < 0:
                    l += 1
                else:
                    r -= 1

        return result
            
    # skip duplicates instead of adding and then scanning result array O(n)