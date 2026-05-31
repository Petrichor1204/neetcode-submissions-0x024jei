class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest substring, where every element is appearing just once
        # edge case: "x", "xxxx"
        #         
        # "abcabcbb"
        #         l
        #         r
        # r=6
        # curr_max = 3
        # maximum = 3
        # sub = s[l:r]
        # keep track of current substring
        # while loop to move l until duplicate is out
        l, r = 0, 0
        maximum = 0
        while r < len(s):
            # find the substring
            
            while s[r] in s[l:r]:
                l += 1
            
            curr_max = (r - l) + 1
            maximum = max(maximum, curr_max)
            r += 1
        return maximum
            