import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        min_heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(min_heap)

        for i in range(k):
            val, key = heapq.heappop(min_heap)
            result.append(key)


        return result