class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tupset = set(tuple(sorted(word)) for word in strs)
        tupdict = {}
        for word in strs:
            if tuple(sorted(word)) in tupdict:
                tupdict[tuple(sorted(word))].append(word)
            else:
                tupdict[tuple(sorted(word))] = [word]
        return list(tupdict.values())