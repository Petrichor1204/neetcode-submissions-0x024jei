class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #so we could create sorted tuples of the strings and compare 
        #them but that would be an O(n2) solution so we create hash
        #tables for the strings instead since that would only loop through
        #the string once.
        #but first, since two strings with different lengths aren't
        #anagrams of each other, we can eliminate that condition
        if len(s) != len(t):
            return False
        
        countS, countT= {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT