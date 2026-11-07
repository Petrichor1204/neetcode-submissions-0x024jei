import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return the kth largest element without sorting
        # use a max heap and return the element on top 
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        for i in range(k):
            ans = heapq.heappop(max_heap)

        return -ans
        
    

    