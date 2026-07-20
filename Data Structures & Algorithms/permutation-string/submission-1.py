from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # goal: to return true if a permutation of s1 is a substring in s2
        # permutations of a word have same characters but diff arrangements
        # s1="adc" s2="dcda"
        #               l
        #                 r
        # abccabee
        # first get the letters we need from s1
        # window to stay at size of s1 throughout
        # {a:1, d:1, c:2}
        # {d:1, c:1, a:1}
        if len(s1) > len(s2):
            return False

        letters = Counter(s1)
        # then go through s2 to get the substring with all the letters
        l = 0
        substring = {}
        for r in range(len(s2)):
            char = s2[r]

            if (r - l + 1) > len(s1):
                if s2[l] in substring:
                    substring[s2[l]] -= 1
                    if substring[s2[l]] == 0:
                        del substring[s2[l]]
                l += 1 

            # if char in s1 add to substring map
            if char in letters:
                substring[char] = substring.get(char, 0) + 1

            if letters == substring:
                return True

        return False
