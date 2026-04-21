class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [2,3,4,5,8,9] target = 
        #  l
        #          r
        # cannot have the same index
        # if bigger than target, move r
        # if smaller than target move l
        # [l + 1, r + 1]
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1

            
