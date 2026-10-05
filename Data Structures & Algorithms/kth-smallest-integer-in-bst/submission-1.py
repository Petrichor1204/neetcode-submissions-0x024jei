# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return the kth smallest value of bst
        # start counting at lowest val left subtree
        # dfs(2.left) -> dfs(1) -> None
        # count = 1
        count = 0
        result = None
        def dfs(node):
            nonlocal count
            nonlocal result
            if not node:
                return None

            dfs(node.left)
            
            count += 1
            if count == k:
                result = node.val

            dfs(node.right)

            

        dfs(root)
        return result

