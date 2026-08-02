from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return true if two trees share the same structure and values
        # add both roots to queues
        # [4,4]
        # 
        if p and not q:
            return False
        if q and not p:
            return False

        if not p and not q:
            return True

        p_queue = deque([p])
        q_queue = deque([q])
        
        while p_queue and q_queue:

            # if vals are unequal return false
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if p_node.val != q_node.val:
                return False

            # otherwise add children and continue
            # if p has left but q doesn't return false and vice versa
            if p_node.left and not q_node.left:
                return False
            if not p_node.left and q_node.left:
                return False

            if p_node.right and not q_node.right:
                return False
            if not p_node.right and q_node.right:
                return False

            if p_node.left:
                p_queue.append(p_node.left)
            if p_node.right:
                p_queue.append(p_node.right)

            if q_node.left:
                q_queue.append(q_node.left)
            if q_node.right:
                q_queue.append(q_node.right)
            
            # return true if both queues are empty
        return not p_queue and not q_queue

