# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # returning the preorder traversal of a roots nodes values
        # preorder = root -> left -> right
        # base case = at the leaf -> if none
        result = []
        def dfs(node):
            if not node:
                return
            # recursive call
            # add the root value
            result.append(node.val)
            
            # call the left value
            dfs(node.left)
            # call the right value
            dfs(node.right)

        dfs(root)
        return result