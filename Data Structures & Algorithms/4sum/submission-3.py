class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums = [3,2,3,-3,1,0], target = 3
        #        [-3,0,1,2,3,3]
        
        # nums=[1,0,-1,0,-2,2] target=0
        #      nums=[2,2,2,2,2] target=8
        #            i
        #              j
        #                l
        #                  r
        # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        # if sum < target: l += 1
        # if sum >= target: r -= 1
        # if sum > target: break
        # [[-3,0,3,3],[-3,1,2,3]]
        # skip duplicates
        nums.sort()
        result = []
        for i in range(len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    
                    # get the current sum
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # only skip duplicates when you have found the target
                        # check if l is at duplicate
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        # check if r is at duplicate
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                            
                    elif curr_sum < target:
                        l += 1
                    else: 
                        r -= 1

        return result

                