class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # goal: return all the diff ways we can arrange nums
        # we have to include every num in nums
        # nums = [1,2,3]
        #         i
        #             j 
        # [3]    
        
        result = []
        
        # backtracking
        def backtrack(i, perm):
            # termination
            if len(perm) == len(nums):
                result.append(list(perm))
                return 
            
            # continuation
            for j in range(len(nums)):
                if nums[j] in perm:
                    continue
                perm.append(nums[j])
                backtrack(j + 1, perm)
                perm.pop()




        backtrack(0, [])
        return result
