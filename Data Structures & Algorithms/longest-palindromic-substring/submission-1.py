class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return the longest substring of s that is a palindrome
        # instead of checking from the ends, do from the center
        def getLength(l, r):
            length = (0,0)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = (l, r)
                l -= 1 
                r += 1
            return length 

        # s = "ababd" length = (1,3)     maxL = (3, aba)
        #          i
        #         l
        #         r
        maxLength = (0, "")
        for i in range(len(s)):
            # odd length
            l, r = getLength(i, i)
            if r - l + 1 > maxLength[0]:
                maxLength = (r - l + 1, s[l: r + 1])

            # even length 
            l, r = getLength(i, i + 1)
            if r - l + 1 > maxLength[0]:
                maxLength = (r - l + 1, s[l: r + 1])

        return maxLength[1]

