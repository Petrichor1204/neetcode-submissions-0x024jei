# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we want to check if each subtree is a valid binary tree as well as the overall tree itself
        # instead of checking from the bottom up, we check from the top down with boundaries

        def dfs(node, left_bound, right_bound):
            if not node:
                return True

            if not (left_bound < node.val < right_bound):
                return False

            return dfs(node.left, left_bound, node.val) and dfs(node.right, node.val, right_bound)


        return dfs(root, float('-inf'), float('inf'))