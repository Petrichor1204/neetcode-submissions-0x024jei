from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        q.append((0, -1))

        visited.add(0)

        while q:
            node, parent = q.popleft()
            
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                visited.add(neigh)
                q.append((neigh, node))
                

        return len(visited) == n
                
        

        