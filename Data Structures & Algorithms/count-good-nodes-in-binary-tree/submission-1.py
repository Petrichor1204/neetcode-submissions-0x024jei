# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count the number of nodes in the tree path that have no bigger preceding nodes
        # at each node, compare with most recent biggest node

        def dfs(root, biggest):
            # base case no node
            if not root:
                return 0

            if root.val >= biggest:
                res = 1
            else:
                res = 0

            biggest = max(biggest, root.val)

            # subproblems - left and right
            res += dfs(root.left, biggest)
            res += dfs(root.right, biggest)
            
            return res

        return dfs(root, root.val)
       


        