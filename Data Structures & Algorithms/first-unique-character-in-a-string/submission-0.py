from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # neetcodeislove
        # i
        # {n:0, e:4, t:1, ...}
        counts = Counter(s)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1
