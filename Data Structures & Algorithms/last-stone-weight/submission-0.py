import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [-1]
        #  i
        # a = -2   b = -2
        # if we use sorting, then every time we get a new value, we'd have to resort
        # best to use heap
        # negate the stones and turn into min heap
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            # pop two stones from the heap at the top
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            # turn them to positive and compare
            if -a > -b:
                new = a - b
                heapq.heappush(max_heap, new)
        # return last stone or none if heap is empty
        return -max_heap[0] if max_heap else 0

