from collections import deque, defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # goal: return the edge to remove to make the graph connected noncyclical
        # a vertex in a cycle has at least two edges
        q = deque()
        adj = defaultdict(list)
        n = len(edges)

        # [0,2,2,2,2]
        # {1:[2,3], 2:[1,4], 3:[1,4], 4:[3,2]}

        indegree = [0] * (n + 1)
        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj[v].append(u)
            adj[u].append(v)

        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)

        # [2,5]
        while q:
            curr = q.popleft()
            indegree[curr] -= 1
            for neigh in adj[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1:
                    q.append(neigh)
        
        for u, v in reversed(edges):
            if indegree[u] >= 2 and indegree[v]:
                return [u, v]

        



                
 
        