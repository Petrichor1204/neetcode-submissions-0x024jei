from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # goal: is to return the maximum number in each window as the window 
        # moves from the left to the right with a size of k
        # nums=[7,2,4]. k=2
        #         l
        #           r
        # queue = [2]
        # res.  = [7,4]
        # every element we see add to q
        # goal is for biggest element to be on top
        q = deque()
        l = 0
        result = []
        for r in range(len(nums)):
            # add the current element to the queue
            if q and q[0] < l:
                q.popleft()

            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            # when we get our window size
            if (r - l + 1) == k:
                result.append(nums[q[0]])
                l += 1
                    
        return result




