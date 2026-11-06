class Solution:
    def longestPalindrome(self, s: str) -> str:
        # checking if palindrome
        # checking the longest
        # s = "ababd"
        #          i
        #          j
        # length = [3, "aba"]
        max_length = [0, ""]

        def isPalindrome(s):
            if s == s[::-1]:
                return True

        for i in range(len(s)):
            for j in range(len(s)):
                if isPalindrome(s[i: j+1]):
                    if (j - i + 1) > max_length[0]:
                        max_length = [(j - i + 1), s[i: j + 1]]

        return max_length[1]


