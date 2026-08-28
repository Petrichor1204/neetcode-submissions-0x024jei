class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # we have to return all the permutations of nums where nums could have duplicates
        # [2,2] i = 0, j = 0,1
        # [] {0,}
        # [2,2]
        nums.sort()
        result = []

        # backtracking
        def backtrack(i, sublist, seen):
            # termination

            if len(sublist) == len(nums):
                result.append(list(sublist))
                return 

            # continuation
            for j in range(len(nums)):
                if j in seen:
                    continue
                if j > 0 and nums[j] == nums[j - 1] and (j - 1) not in seen:
                    continue
                sublist.append(nums[j])
                seen.add(j)
                backtrack(i + 1, sublist, seen) 
                sublist.pop()
                seen.remove(j)

        backtrack(0, [], set())
        return result

        