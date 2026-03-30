class Solution:
    #i'm going to iterate through the list to see if there's any value
    #that appears more than once. i'm going to use a for loop
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False       
                   
