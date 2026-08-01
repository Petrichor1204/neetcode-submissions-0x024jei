# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return the diameter of a binary tree where the diameter is the length of 
        # the longest path between any two nodes and the length is the num of edges
        # l = 0
        # d = 0
        diameter = 0
       
        def dfs(node):
            nonlocal diameter
            # base case - if not node return 
            if not node:
                return 0
            
            # subproblems - left length, right length
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)


        # return helper variable
        dfs(root)
        return diameter


