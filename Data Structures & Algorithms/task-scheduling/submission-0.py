from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # goal: return the min cycles to complete all tasks
        # tasks = ["X","X","Y","Y"], n = 2
        # heap = [, ] -1 q = [] cycles = 5
        freq = Counter(tasks) 
        pq = [-count for count in freq.values()]
        print(pq)

        heapq.heapify(pq)
        q = deque()
        cycles = 0

        while pq or q:
            cycles += 1

            if pq:
                count = heapq.heappop(pq)

                count += 1
                if count != 0:
                    q.append((count, cycles + n))

            if q and q[0][1] == cycles:

                heapq.heappush(pq, q.popleft()[0])

        return cycles


