class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) #to make sure every element is unique
        longest = 0 #for cases where there's no cons. seq.

        for num in numset:
            if (num - 1) not in numset:
                length = 1 #to keep track of the longest sequence
                while (num + length) in numset: #to get the length of each sequence if there's one.
                    length += 1
                longest = max(longest, length) #to cater for edge cases and return whatever value's bigger.
        return longest





