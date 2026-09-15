from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # goal: return a valid order of courses i need to take so that i can finish all my courses
        # numCourses=2 prerequisites=[[0,1]]
        result = []
        completed = 0
        indegree = [0] * numCourses #[0,0] {1: [0]} []
        pre_map = defaultdict(list)
        q = deque()

        for u, v in prerequisites:
            indegree[u] += 1
            pre_map[v].append(u)

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            result.append(course)
            completed += 1
            for n in pre_map[course]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)            

        return result if completed == numCourses else []
                



        

        
