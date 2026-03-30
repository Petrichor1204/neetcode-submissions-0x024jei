class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #have same number of each letter but order is different
        if len(s) != len(t):
            return False
        freq_s = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
 
        for char in t:
            if char in freq_s:
                freq_s[char] -= 1
                if freq_s[char] == 0:
                    del freq_s[char]
        return not freq_s
