import heapq
from collections import deque
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # goal: create a string s using at most a, b, c number of a b and c's
        # return the longest happy string, meeting the ff conditions:
        # only contains letters a b and c - dont add any other letter
        # no three consecutive letter substrings - at most consec is 2
        # at most a, b and c occurences - keep adding until limit
        # longest = sum(a, b, c)
        # a = 0, b = 1, c = 5
        # max_heap = [ ] q = [,(-1, c) ] res = ccbcc  temp = 
        max_heap = [(-a, "a"), (-b, "b"), (-c, "c")] 
        heapq.heapify(max_heap)
        res = ""
        temp = (0, "")

        while max_heap:
            curr, char = heapq.heappop(max_heap)
            if curr == 0:
                continue
            if len(res) > 1 and res[-2:] == (char * 2):
                temp = (curr, char)
                if not max_heap:
                    break
                curr, char = heapq.heappop(max_heap)
                if curr == 0:
                    continue

            res += char
            curr += 1
                
            if curr < 0:
                heapq.heappush(max_heap, (curr, char))

            if temp[0] != 0:
                heapq.heappush(max_heap, temp)
                temp = (0, "")
                
        return res





        