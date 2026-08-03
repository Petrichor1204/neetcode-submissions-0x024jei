class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # goal: find two nums on diff indexes that are eq to each other
        # nums = [1,2,3,1], k = 1
        #         i
        # {1:[0,3], 2:[1], 3:[2]}              

        num_to_idx = {}

        for i, n in enumerate(nums):
            if n in num_to_idx:
                num_to_idx[n].append(i)
            else:
                num_to_idx[n] = [i]

        for i in range(len(nums)):
            if nums[i] in num_to_idx:
                for j in num_to_idx[nums[i]]:
                    if i != j and abs(i - j) <= k:
                        return True
                    continue
        return False
                





        