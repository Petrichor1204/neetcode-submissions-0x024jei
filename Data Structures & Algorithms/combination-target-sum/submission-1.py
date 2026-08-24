class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # goal: given a target num i should return a list of lists where each list contains the various combs of nums in nums that add up to the target
        # sorting the input
        nums.sort()
        total = 0
        result = []
       
        # backtracking
        def backtrack(i, curr_nums): #target = 5
            nonlocal total 

            # termination - when sum >= target
            if total == target:
                result.append(curr_nums.copy())
                return 
            elif total > target:
                return 

            # continuation - try with other nums
            for j in range(i, len(nums)):
                # while total < target:
                if nums[j] + total > target:
                    continue
                total += nums[j]
                curr_nums.append(nums[j])

                backtrack(j, curr_nums)
                num = curr_nums.pop()
                total -= num


        backtrack(0, [])
        return result
