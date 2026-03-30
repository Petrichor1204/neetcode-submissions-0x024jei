class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        r = 0
        tracker = set()
        while r < len(s):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
                
            if s[r] not in tracker:
                tracker.add(s[r])
            longest = max(longest, (r - l)+ 1)
            r += 1
        return longest

