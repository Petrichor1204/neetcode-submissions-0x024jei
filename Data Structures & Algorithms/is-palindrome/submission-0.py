class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(char for char in s if char.isalnum())
        l = 0
        r = len(new_s) - 1
        while l < r:
            if new_s[l].lower() == new_s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True