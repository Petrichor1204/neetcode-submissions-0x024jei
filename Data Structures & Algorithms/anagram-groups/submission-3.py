class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string and group with hash map
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

        return list(anagrams.values())
