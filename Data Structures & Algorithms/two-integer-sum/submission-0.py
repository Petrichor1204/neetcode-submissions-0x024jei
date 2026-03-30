class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}
        for i, n in enumerate(nums):
            summ[n] = i
        for i, n in enumerate(nums):
            difference = target - n
            if difference in summ and summ[difference] != i:
                return  [i, summ[difference]]
