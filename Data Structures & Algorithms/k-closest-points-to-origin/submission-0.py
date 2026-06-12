import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # goal: to return the k points that are closest to the origin
        # points = [[0,2],[2,2]], k = 1
        min_heap = [] #[(2,0,2), (2,2,0), (2,82,2,2)]
        
        for x, y in points:
            distance = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(min_heap, (distance, x, y))
            
        res = []
        i = 0
        while i < k:
            distance, x, y = heapq.heappop(min_heap) #
            res.append([x, y])
            i += 1

        return res

