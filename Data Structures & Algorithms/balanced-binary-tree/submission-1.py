# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node):
            nonlocal balanced
            # base case = empty node
            if not node:
                return 0

            # subproblem = left and right heights
            left = dfs(node.left)
            right = dfs(node.right)

            # connect = abs(left height - right height) < 2 == true
            balanced = balanced and abs(left - right) < 2

            # return height = 1 + max(left, right)
            return 1 + max(left, right)

        dfs(root)
        return balanced
