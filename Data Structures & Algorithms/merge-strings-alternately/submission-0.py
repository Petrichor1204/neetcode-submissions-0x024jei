class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merge two given strings alternatively
        # word1 = "abc", word2 = "xyz"
        #          i
        #                         j
        i, j = 0, 0
        merged = []
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        merged += word1[i:]
        merged += word2[j:]
        return "".join(merged)

