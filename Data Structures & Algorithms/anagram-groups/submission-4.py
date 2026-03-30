class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using counter to get frequency of each character
        #then compare with other words, if same, group
        anagrams = defaultdict(list)
        
        # for each word, take each character
        for word in strs:
            letters = [0] * 26
            for c in word:
                letters[ord(c) - ord("a")] += 1

            anagrams[tuple(letters)].append(word)

        return list(anagrams.values())

