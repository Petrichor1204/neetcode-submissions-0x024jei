from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree - one fully connected component, has no cycles
        # n=5       edges=[[0,1],[2,1],[3,2],[3,1],[4,1]]
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def isOne(edges, adj):
            q = deque()
            visited = set()

            components = 0
            for node in range(n):
                if node not in visited:
                    q.append(node)
                    components += 1
                    while q:
                        curr = q.popleft()
                        visited.add(curr)
                        for neigh in adj[curr]:
                            if neigh not in visited:
                                q.append(neigh)
            if components == 1:
                return True
            return False

        def isNotCycle(adj, edge, n):
            indegree = [0] * n
            for u, v in edges:
                indegree[u] += 1
                indegree[v] += 1

            q = deque()
            for i in range(len(indegree)):
                if indegree[i] == 1:
                    q.append(i)

            while q:
                node = q.popleft()
                for neigh in adj[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        q.append(neigh)
        
            for u, v in edges:
                if indegree[u] == 2 and indegree[v]:
                    return False
            return True     
            
            

        return isOne(edges, adj) and isNotCycle(adj, edges, n)
            

                    


            

                
       

