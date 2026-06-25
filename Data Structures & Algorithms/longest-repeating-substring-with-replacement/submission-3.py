class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # goal: is to replace at most k characters in the string with another character
        # that will give us the longest substring in the string and return that length
        #  s="ABAA"  k = 0
        #       l
        #         r
        # expand the window: 
        # shrink the window:
        # keep max_window
        # {A:2,B:0}
        # mc = A
        l = 0
        max_window = 0
        freq = {}
        max_count = 0
        for r in range(len(s)):
            char = s[r]
            freq[char] = freq.get(char, 0) + 1 
            if freq[char] > max_count:
                max_count = freq[char]
                max_char = char
            if (r - l + 1) - max_count > k:
                freq[s[l]] -= 1
                l += 1
                

            max_window = max(max_window, (r - l) + 1)
   
        return max_window