from collections import deque, defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # goal: return the number of connected components in the graph
        # n = 5, edges = [[0,1],[1,2],[3,4]]
        # {0:[1], 1:[2,0], 2:[1], 3:[4], 4:[3]}
        visited = set()
        adj = defaultdict(list)
        count = 0
        q = deque()
        # q = []
        # visited = {0,1,2,3,4}
        # count = 2

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for node in range(n):
            if node not in visited:
                q.append(node)
                while q:
                    node = q.popleft()
                    visited.add(node)
                    for neigh in adj[node]:
                        if neigh not in visited:
                            q.append(neigh)
                count += 1
            

        return count



