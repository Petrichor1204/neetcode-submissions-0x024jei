from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # adjList = [[2],[1,3],[2]] 2, 1, 3
        # q = [3] 2
        # otn = {1: [1], 2: [2], 3: [3]} 1, [2] -> 2, [1, 3]
        if not node:
            return None
        q = deque([node])
        old_to_new = {}
        while q:
            curr = q.popleft()
            if curr not in old_to_new:
                old_to_new[curr] = Node(curr.val)
            new_node = old_to_new[curr]
            for neigh in curr.neighbors:
                if neigh not in old_to_new:
                    old_to_new[neigh] = Node(neigh.val)
                    q.append(neigh)
                new_neigh = old_to_new[neigh]
                new_node.neighbors.append(new_neigh)
                
        new_node = old_to_new[node]
        return new_node