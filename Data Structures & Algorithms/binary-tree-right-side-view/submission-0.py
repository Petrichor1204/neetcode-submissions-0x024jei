from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(node.val)
        return result
        






        # return the values that are visible from the right side of the tree
        # two scenarios: all the right values if the tree is balanced/right > left
        # the right values + the extra left values in unbalanced tree
        # result = []
        # def dfs(root):

        #     if not root:
        #         return 
        
        #     result.append(root.val)

        #     # if no right subtree
        #     if not root.right:
        #         dfs(root.left)


        #     # has left and right
        #     dfs(root.right)

        #     dfs(root.left.left)
        
        # dfs(root)
        # return result


       