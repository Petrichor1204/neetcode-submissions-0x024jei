class Solution:
    def countSubstrings(self, s: str) -> int:
        # count the number of palindromic substrings in a string
        # s = "aaa" res = 6  rs = 
        #        i
        #        l
        #         r
        def expandPalindrome(res, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
            
        res = 0
        for i in range(len(s)):
            # odd length
            res += expandPalindrome(0, i, i)

            # even length 
            res += expandPalindrome(0, i, i + 1)

        return res

        
            