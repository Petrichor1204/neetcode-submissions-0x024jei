from collections import deque
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # neetcodeneet
        #         i
        # [0,1,2,3,4,5,6,7,8]
        # {n:1, e:1, t:1, ...}
        # why queue = to maintain the order of items
        # how would you use a queue
            # for every character, add to queue
            # get its count
            # check char at front if count > 1, pop from queue
            # then move on to next char
            # at end, return first char in queue
        # baab
        # []
        q = deque()
        counts = {}
        for i in range(len(s)):
            q.append(i)
            counts[s[i]] = counts.get(s[i], 0) + 1
            while q and counts[s[q[0]]] > 1:
                q.popleft()
        return q[0] if q else -1

