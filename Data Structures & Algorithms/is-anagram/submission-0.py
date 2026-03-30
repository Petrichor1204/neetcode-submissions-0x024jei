class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tup1 = sorted(tuple(s))
        tup2 = sorted(tuple(t))
        if tup1 == tup2:
            return True
        return False 
