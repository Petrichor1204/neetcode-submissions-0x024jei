# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # return the inorder traversal of a tree's node values
        # inorder: left -> root -> right
        # [f(1) -> f(3) -> f(7) -> r]
        # [4, 2, 5, 1, 6, 3, 7]
        # base case -> at leaf node
        result = []

        def dfs(node):
            if not node:
                return

            # recursive case
            # call the left
            dfs(node.left)
            result.append(node.val)
            # call the right
            dfs(node.right)
            

        dfs(root)
        return result
