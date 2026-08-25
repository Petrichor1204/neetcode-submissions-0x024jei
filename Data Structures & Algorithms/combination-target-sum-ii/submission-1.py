class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # goal: to find all the possible combinations of numbers in candidates that sum up to the target
        # skip duplicates
        # [1,2,2,4,5,6,9]
        candidates.sort()
        result = []
        total = 0
        #backtracking
        def backtrack(i, curr_list):
            nonlocal total
            
            # termination
            if total == target:
                result.append(curr_list.copy())
                return
            
            # continuation
            for j in range(i, len(candidates)):  
                if total + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                curr_list.append(candidates[j])
                total += candidates[j]
                backtrack(j + 1, curr_list)
                num = curr_list.pop()
                total -= num

        backtrack(0, [])
        return result

