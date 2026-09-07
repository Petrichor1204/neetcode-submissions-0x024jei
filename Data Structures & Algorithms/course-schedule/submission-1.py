from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # goal: return true if can finish al courses else false
        # numCourses=3
        # prerequisites=[[1,0],[1,2],[0,1]]
        # [1,1,0] {0:[1], 2:[1], 1:[0]} {2} [] 
        indegree = [0] * numCourses
        pre_dict = defaultdict(list)
        visited = set()

        # fill the in and out arr
        for u, v in prerequisites:
            indegree[u] += 1
            pre_dict[v].append(u)
        
        # take all courses without prerequisites
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        # for each course explore neighbors and add neibors to visit later
        while q:
            node = q.popleft()
            visited.add(node)
            neighbors = pre_dict[node]
            for n in neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        # count num visited
        # if visited == initial courses return true else false
        return len(visited) == numCourses