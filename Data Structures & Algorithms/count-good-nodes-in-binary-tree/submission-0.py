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
        count = 0

        def dfs(root, biggest):
            nonlocal count
            # base case no node
            if not root:
                return 

            if root.val >= biggest:
                count += 1
            biggest = max(biggest, root.val)

            # subproblems - left and right
            dfs(root.left, biggest)
            dfs(root.right, biggest)
            

        dfs(root, float('-inf'))
        return count


        