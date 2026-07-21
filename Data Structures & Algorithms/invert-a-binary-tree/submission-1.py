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
        # base case = leaf node
        if not root:
            return

        # swap the nodes
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

    
        return root