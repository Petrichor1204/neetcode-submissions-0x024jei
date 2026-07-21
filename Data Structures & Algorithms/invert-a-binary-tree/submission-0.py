# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # goal: is to laterally invert the tree so that all nodes on the right 
        # go to left and vice versa
        # return the root of inverted tree
        # create a new node from original root
        # 
       
        

        def dfs(node):
            # base case = leaf node
            if not node:
                return

            # swap the nodes
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root