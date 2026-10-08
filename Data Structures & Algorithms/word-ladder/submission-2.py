from collections import defaultdict, deque, Counter

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        INF = float('inf')
        dist = {}
        seen = set()
        if endWord not in wordList:
            return 0
        
        #modeling my input as a graph
        adj = defaultdict(list) #u: [(v, w)]
        wordList = [beginWord] + wordList
       
        for word in wordList:
            dist[word] = INF

        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                word1, word2 = wordList[i], wordList[j]
                diff = sum(c1 != c2 for c1, c2 in zip(word1, word2))
                if diff == 1:
                    adj[word1].append((word2, 1))
                    adj[word2].append((word1, 1))


        q = deque([(beginWord, 1)])

        while q:
            word, d = q.popleft()
           
            seen.add(word)
                
            for nei, val in adj[word]:
                if nei not in seen:
                    if d + val < dist[nei]:
                        dist[nei] = d + val
                        q.append((nei, dist[nei]))
        
        return dist[endWord] if dist[endWord] != INF else 0
