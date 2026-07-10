class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # goal: is to return the node that does not point to anyone but
        # has everyone in n except itself pointing to it
        # [[1,3],[4,3],[2,3]] n = 4 [0,0,3,0] n - 1 [0,0,0,0]
        indegree = [0] * (n + 1) #[]
        outdegree = [0] * (n + 1)

        for k, v in trust: 
            indegree[v] += 1
            outdegree[k] += 1


        for i in range(1, n+1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i 

        return -1

